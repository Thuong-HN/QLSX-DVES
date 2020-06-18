using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;
using System.Timers;
using MySql.Data.MySqlClient;

namespace QLSX.Service
{
    public partial class Service1 : ServiceBase
    {
        Timer timer = new Timer();
        String Textsave = "";
        string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=qlsx_dves;";
        string query = "SELECT * FROM save_data";

        private Socket m_sock;                      // Server connection
        private byte[] m_byBuff = new byte[1024];    // Recieved data buffer

        private String auto, timepush, id;


        public Service1()
        {
            InitializeComponent();
            connected();
            
        }

        protected override void OnStart(string[] args)
        {
            //getData();
            WriteToFile("Service is start... AT: " + DateTime.Now);
            timer.Elapsed += new ElapsedEventHandler(OnElapsedTime);
            timer.Interval = 5000; //number in milisecinds  
            timer.Enabled = true;
        }

        protected override void OnStop()
        {
            WriteToFile("Service is stopped AT:  " + DateTime.Now);
            WriteToFile("----------------------------------------");
        }
        private void OnElapsedTime(object source, ElapsedEventArgs e)
        {
            //getData();
            //WriteToFile("Service is recall at " + DateTime.Now);
            WriteToFile("Service is running... AT: " + DateTime.Now);
        }


        private void connected()
        {
           
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
                
                    //MessageBox.Show(this, "Unable to connect to remote machine", "Connect Failed!");
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "Unusual error during Connect!");
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
                    string[] tokens = sRecieved.Split(',');

                    auto = tokens[0]; timepush = tokens[1];id = tokens[2];
                    insertData();
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
        
        public void SetupRecieveCallback(Socket sock)
        {
            try
            {
                AsyncCallback recieveData = new AsyncCallback(OnRecievedData);
                sock.BeginReceive(m_byBuff, 0, m_byBuff.Length, SocketFlags.None, recieveData, sock);
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "Setup Recieve Callback failed!");
            }
        }





        private void insertData()
        {
            string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=qlsx_dves;";
            string query = "INSERT INTO save_data(`Auto`, `Time Push`, `ID`) VALUES ('" + auto + "','" + timepush + "','" + id + "')";
            // Which could be translated manually to :
            // INSERT INTO user(`id`, `first_name`, `last_name`, `address`) VALUES (NULL, 'Bruce', 'Wayne', 'Wayne Manor')

            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            commandDatabase.CommandTimeout = 60;

            try
            {
                databaseConnection.Open();
                MySqlDataReader myReader = commandDatabase.ExecuteReader();

                
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                // Show any error message.
               
            }
        }
        private void updateUser()
        {
            string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=qlsx_dves;";
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
               
            }
        }
        public void WriteToFile(string Message)
        {
            string path = AppDomain.CurrentDomain.BaseDirectory + "\\Logs";
            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }
            string filepath = AppDomain.CurrentDomain.BaseDirectory + "\\Logs\\ServiceLog_" + DateTime.Now.Date.ToShortDateString().Replace('/', '_') + ".txt";
            if (!File.Exists(filepath))
            {
                // Create a file to write to.   
                using (StreamWriter sw = File.CreateText(filepath))
                {
                    sw.WriteLine(Message);
                }
            }
            else
            {
                using (StreamWriter sw = File.AppendText(filepath))
                {
                    sw.WriteLine(Message);
                }
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
                        string[] row = { reader.GetString(0)};
                        if (row[0] != "")
                        {
                            Textsave = "LOG-EVENT START: ";
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
               
            }
        }


    }
}
