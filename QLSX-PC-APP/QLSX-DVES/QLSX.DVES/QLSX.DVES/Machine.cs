using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

/*
 *  DEV by Thuonghuynh
 */
// Declare the delegate prototype to send data back to the form
//delegate void AddMessage(string sNewMessage);
//delegate void SetTextCallback(string text);
namespace QLSX.DVES
{
    public partial class Popup_Machine : Form
    {
        // Change the username, password and database according to your needs
        // You can ignore the database option if you want to access all of them.
        // 127.0.0.1 stands for localhost and the default port to connect.
        string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=test;";
        // Your query,
        string query = "SELECT * FROM testcreate";

        //private Container _components = null;
        // My Attributes
        private Socket m_sock;                      // Server connection
        private byte[] m_byBuff = new byte[1024];    // Recieved data buffer
        private event AddMessage m_AddMessage;              // Add Message Event handler for Form

        public Popup_Machine()
        {
            InitializeComponent();
            // ************ FULL SCREEN ***************************************
            //this.TopMost = true;
            //this.FormBorderStyle = FormBorderStyle.SizableToolWindow;//.None;
            //this.FormBorderStyle = FormBorderStyle.Fixed3D;
            //this.WindowState = FormWindowState.Maximized;
            // ****************************************************************
            //insertData();
            
            //getData();

            connected();
            // Add Message Event handler for Form decoupling from input thread
            m_AddMessage = new AddMessage(OnAddMessage);

        }
        private void FormMain_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            if (m_sock != null && m_sock.Connected)
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
            }
        }
        private void SetText(string text)
        {
            // InvokeRequired required compares the thread ID of the
            // calling thread to the thread ID of the creating thread.
            // If these threads are different, it returns true.
            if (this.lblKWH.InvokeRequired)
            {
                SetTextCallback d = new SetTextCallback(SetText);
                this.Invoke(d, new object[] { text });
            }
            else
            {
                this.lblKWH.Text = text;
            }
        }
        // *********************** CONNECTING... *********************************
        private void connected()
        {
            Cursor cursor = Cursor.Current;
            Cursor.Current = Cursors.WaitCursor;
            try
            {
                // Close the socket if it is still open
                if (m_sock != null && m_sock.Connected)
                {
                    m_sock.Shutdown(SocketShutdown.Both);
                    System.Threading.Thread.Sleep(10);
                    m_sock.Close();
                }

                // Create the socket object
                m_sock = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

                // Define the Server address and port
                IPEndPoint epServer = new IPEndPoint(IPAddress.Parse("192.168.2.244"), 80);

                // Connect to the server blocking method and setup callback for recieved data
                // m_sock.Connect( epServer );
                // SetupRecieveCallback( m_sock );

                // Connect to server non-Blocking method
                m_sock.Blocking = false;
                AsyncCallback onconnect = new AsyncCallback(OnConnect);
                m_sock.BeginConnect(epServer, onconnect, m_sock);
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "Server Connect failed!");
            }
            Cursor.Current = cursor;
        }
        public void OnConnect(IAsyncResult ar)
        {
            // Socket was the passed in object
            Socket sock = (Socket)ar.AsyncState;

            // Check if we were sucessfull
            try
            {
                //sock.EndConnect( ar );
                if (sock.Connected)
                    SetupRecieveCallback(sock);
                else
                    MessageBox.Show(this, "Unable to connect to remote machine", "Connect Failed!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(this, ex.Message, "Unusual error during Connect!");
            }
        }
        public void OnRecievedData(IAsyncResult ar)
        {
            // Socket was the passed in object
            Socket sock = (Socket)ar.AsyncState;

            // Check if we got any data
            try
            {
                int nBytesRec = sock.EndReceive(ar);
                if (nBytesRec > 0)
                {
                    // Wrote the data to the List
                    string sRecieved = Encoding.ASCII.GetString(m_byBuff, 0, nBytesRec);

                    // WARNING : The following line is NOT thread safe. Invoke is
                    // m_lbRecievedData.Items.Add( sRecieved );

                    Invoke(m_AddMessage, new string[] { sRecieved });

                    // If the connection is still usable restablish the callback
                    SetupRecieveCallback(sock);
                }
                else
                {
                    // If no data was recieved then the connection is probably dead
                    //Console.WriteLine("Client {0}, disconnected", sock.RemoteEndPoint);
                    sock.Shutdown(SocketShutdown.Both);
                    sock.Close();
                }
            }
            catch (InvalidOperationException exc)
            {
                //MessageBox.Show(exc.ToString());
            }

            catch (Exception exception)
            {
                //MessageBox.Show(exception.Message);
            }
        }

        // *********************** RECV DATA *********************************
        private int kwh;
        public void OnAddMessage(string sMessage)
        {
            SetText(sMessage);
            try
            {
                string[] tokens = sMessage.Split(',');

                lbl_ID.Text = tokens[2];
                String getKwh = tokens[13].Substring(2);
                kwh = getKwh.CompareTo(getKwh);

                lblKWH.Text = getKwh;
                
                //foreach (string line in tokens)
                //{
                //    MessageBox.Show(line);
                //}
                //senData(); // RESPONE
            }
            catch (Exception ex)
            {
                MessageBox.Show(this, ex.Message, "Setup Recieve Callback failed!");
            }

        }
        public void SetupRecieveCallback(Socket sock)
        {
            try
            {
                AsyncCallback recieveData = new AsyncCallback(OnRecievedData);
                sock.BeginReceive(m_byBuff, 0, m_byBuff.Length, SocketFlags.None, recieveData, sock);
            }
            catch (Exception ex)
            {
                MessageBox.Show(this, ex.Message, "Setup Recieve Callback failed!");
            }
        }

        // *********************** SEND *********************************
        private void senData()
        {
            // Check we are connected
            if (m_sock == null || !m_sock.Connected)
            {
                MessageBox.Show(this, "Must be connected to Send a message");
                return;
            }

            // Read the message from the text box and send it
            try
            {
                // Convert to byte array and send.
                Byte[] byteDateLine = Encoding.ASCII.GetBytes("Respone OK".ToCharArray());
                m_sock.Send(byteDateLine, byteDateLine.Length, 0);
            }
            catch (Exception ex)
            {
                MessageBox.Show(this, ex.Message, "Send Message Failed!");
            }
        }





        
        private void insertData()
        {
            string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=test;";
            string query = "INSERT INTO testcreate(`id`, `First_Name`, `Time_start`) VALUES (NULL, '" + "Nguyen Van A" + "', '" + "10:00" + "')";
            // Which could be translated manually to :
            // INSERT INTO user(`id`, `first_name`, `last_name`, `address`) VALUES (NULL, 'Bruce', 'Wayne', 'Wayne Manor')

            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            commandDatabase.CommandTimeout = 60;

            try
            {
                databaseConnection.Open();
                MySqlDataReader myReader = commandDatabase.ExecuteReader();

                MessageBox.Show("User succesfully registered");

                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                // Show any error message.
                MessageBox.Show(ex.Message);
            }
        }
        private void updateUser()
        {
            string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=test;";
            // Update the properties of the row with ID 1
            string query = "UPDATE `user` SET `first_name`='Willy',`last_name`='Wonka',`address`='Chocolate factory' WHERE id = 1";

            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            commandDatabase.CommandTimeout = 60;
            MySqlDataReader reader;

            try
            {
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();

                // Succesfully updated

                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                // Ops, maybe the id doesn't exists ?
                MessageBox.Show(ex.Message);
            }
        }
        private void getData()
        {
            // Prepare the connection
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            commandDatabase.CommandTimeout = 60;
            MySqlDataReader reader;
            try
            {
                // Open the database
                databaseConnection.Open();
                // Execute the query
                reader = commandDatabase.ExecuteReader();

                // All succesfully executed, now do something

                // IMPORTANT : 
                // If your query returns result, use the following processor :

                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        // As our database, the array will contain : ID 0, FIRST_NAME 1,LAST_NAME 2, ADDRESS 3
                        // Do something with every received database ROW
                        string[] row = { reader.GetString(0), reader.GetString(1), reader.GetString(2) };
                        if (row[1] == "" && row[2] == "")
                        {
                            row[1] = "Nguyen Van A"; row[2] = "10:00";
                        }
                        

                    }
                }
                else
                {
                    Console.WriteLine("No rows found.");
                }

                // Finally close the connection
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                // Show any error message.
                MessageBox.Show(ex.Message);
            }
        }

        private void back_Click(object sender, EventArgs e)
        {
            if (m_sock != null && m_sock.Connected)
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
            }

            MAIN main = new MAIN();
            main.Show();
            this.Close();
        }
    }

}
