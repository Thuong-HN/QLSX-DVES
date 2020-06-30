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


delegate void AddMessage(string sNewMessage);
delegate void SetTextCallback(string text);
namespace QLSX.DVES
{
    public partial class MAIN : Form
    {
    
        string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=qlsx_dves;";
        string query = "SELECT ID FROM `save_realtime`";
        private Socket m_sock = null;                      
        private byte[] m_byBuff = new byte[1024];    
        private event AddMessage m_AddMessage;
        private string auto, timepush, id, s1, s2, onoff, rfid, barcode, amp, freg, maxfreg, counter, timefree, kwhs;
        public MAIN()
        {
            InitializeComponent();
            // ************ FULL SCREEN ***************************************
            //this.TopMost = true;
            //this.FormBorderStyle = FormBorderStyle.SizableToolWindow;//.None;
            //this.FormBorderStyle = FormBorderStyle.Fixed3D;
            //this.WindowState = FormWindowState.Maximized;
            // ****************************************************************
            //insertData();
            KWH();
            //getData();
            connected();



            m_AddMessage = new AddMessage(OnAddMessage);
            
            

        }
        private void FormMain_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            try
            {
                if (m_sock != null && m_sock.Connected)
                {
                    m_sock.Shutdown(SocketShutdown.Both);
                    m_sock.Close();

                }
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
                throw;
            }
            
        }
        
        private void SetText(string text)
        {
            try
            {
                if (this.txtGetdata.InvokeRequired)
                {
                    SetTextCallback d = new SetTextCallback(SetText);
                    this.Invoke(d, new object[] { text });
                }
                else
                {
                    this.txtGetdata.Text = text;
                }
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
                throw;
            }
                 
            
        }
        // *********************** CONNECTING... *********************************
        private void connected()
        {
            //MessageBox.Show(this, "CONNECTING.....");
            Cursor cursor = Cursor.Current;
            Cursor.Current = Cursors.WaitCursor;
			try
			{
                

                if (m_sock != null && !m_sock.Connected)
				{
                     m_sock.Shutdown(SocketShutdown.Both );
					 System.Threading.Thread.Sleep( 2 );
					 m_sock.Close();
                     //pic_stt_connect.Image = Properties.Resources.notconnected;

                }
                
                m_sock = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp );
                IPEndPoint epServer = new IPEndPoint(IPAddress.Parse("192.168.2.244"), 80);
                m_sock.Blocking = false;
				AsyncCallback onconnect = new AsyncCallback(OnConnect);
                m_sock.BeginConnect(epServer, onconnect, m_sock);


            }
			catch(Exception ex )
			{
				//MessageBox.Show( this, ex.Message, "Connected failed!" );
            }
            Cursor.Current = cursor;
        }
        public void OnConnect(IAsyncResult ar)
        {
            Socket sock = (Socket)ar.AsyncState;
            try
            {
                //sock.EndConnect( ar );
                if (sock.Connected)
                {
                    pic_stt_connect.Image = Properties.Resources.connected;
                    SetupRecieveCallback(sock);
                }
                timer1.Start();
            }
            catch (Exception ex)
            {
               // MessageBox.Show(this, ex.Message, "Reconnect");
            }
        }
        static bool IsSocketConnected(Socket s)
        {
            return !((s.Poll(1000, SelectMode.SelectRead) && (s.Available == 0)) || !s.Connected);
            
            /* The long, but simpler-to-understand version:

                    bool part1 = s.Poll(1000, SelectMode.SelectRead);
                    bool part2 = (s.Available == 0);
                    if ((part1 && part2 ) || !s.Connected)
                        return false;
                    else
                        return true;

            */
        }
        public void OnRecievedData(IAsyncResult ar)
        {
            Socket sock = (Socket)ar.AsyncState;
            try
            {
                int nBytesRec = sock.EndReceive(ar);
                if (nBytesRec > 0)
                {
                    string sRecieved = Encoding.ASCII.GetString(m_byBuff, 0, nBytesRec);
                    Invoke(m_AddMessage, new string[] { sRecieved });
                    SetupRecieveCallback(sock);
                }
                
            }
            catch (InvalidOperationException exc)
            {
               // MessageBox.Show(exc.ToString());
            }

            catch (Exception exception)
            {
                //MessageBox.Show(exception.Message);
            }
        }

        // *********************** RECV DATA *********************************
     
        public void OnAddMessage(string sMessage)
        {
            SetText(sMessage);
            try
            {
                string[] tokens = sMessage.Split(',');

                String getKwh = tokens[13].Substring(2);
                int kwh = getKwh.CompareTo(getKwh);

                lblKWH.Text = getKwh;
                chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 1", kwh);
                auto = tokens[0]; timepush = tokens[1]; id = tokens[2]; s1 = tokens[3]; s2 = tokens[4]; onoff = tokens[5]; rfid = tokens[6]; barcode = tokens[7]; amp = tokens[8]; freg = tokens[9];
                maxfreg = tokens[10]; counter = tokens[11]; timefree = tokens[12]; kwhs = getKwh;
                //getData();
                //foreach (string line in tokens)
                //{
                //    MessageBox.Show(line);
                //}
                //SenData(); // RESPONE
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "Setup Recieve Callback failed!");
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
                //MessageBox.Show(this, ex.Message, "Setup Recieve Callback failed!");
            }
        }

        // *********************** SEND *********************************
        private void SenData()
        {
            try
            {
                Byte[] byteDateLine = Encoding.ASCII.GetBytes("APP".ToCharArray());
                m_sock.Send(byteDateLine, byteDateLine.Length, 0);

            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "Send Message Failed!");
            }
        }
        private void timer1_Tick(object sender, EventArgs e)
        {

            try
            {
                //MessageBox.Show(this, m_sock.Connected.ToString());

                if (!IsSocketConnected(m_sock) || m_sock == null || !m_sock.Connected)
                {
                    pic_stt_connect.Image = Properties.Resources.notconnected;
                    connected();
                }
                else
                {
                    //MessageBox.Show(this, "SEND Request DATA");
                    SenData();
                }
                /*
                if (m_sock == null || !m_sock.Connected)
                {
                    //MessageBox.Show(this, "M_SOCK DIS");
                    pic_stt_connect.Image = Properties.Resources.notconnected;
                    connected();
                }
                
                else 
                {
                    
                    //MessageBox.Show(this,  "SENDDATA");
                    SenData();
                }
                */
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR TIMER!");

            }


        }



        private void KWH()
        {
            //int x = 10000;
            //AddXY value in chart1 in series named as Salary  
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 1", "5000");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 2", "8000");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 3", "7000");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 4", "8500");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 5", "10000");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 6", "8500");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 7", "1000");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 8", "9800");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 9", "7000");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 10", "5000");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 11", "6500");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 12", "500");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 13", "1300");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 14", "2000");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 15", "2500");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 16", "4500");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 17", "800");
            chart1.Series["ĐIỆN NĂNG"].Points.AddXY("MÁY 18", "9800");
            //chart title  
            chart1.Titles.Add("GIÁM SÁT ĐIỆN NĂNG");
            

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

                //MessageBox.Show("User succesfully registered");

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

            string query_update = "UPDATE `save_realtime` SET `Auto` = '" + auto + "', `TimePush` = '" + timepush + "', `ID`='" + id + "', `S1`='" + s1 + "', `S2`='" + s2 + "', `On/Off`='" + onoff + "', `RFID`='" + rfid + "', `Barcode`='" + barcode + "', `Amp`='" + amp + "', `Freg`='" + freg + "', `MaxFreg`='" + maxfreg + "', `Counter`='" + counter + "', `TimeFree`='" + timefree + "', `KWH`='" + kwhs + "' WHERE `ID` = '" + id + "' ";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            
            MySqlCommand commandDatabase = new MySqlCommand(query_update, databaseConnection);
            //commandDatabase.CommandTimeout = 60;
            

            try
            {
                databaseConnection.Open();
                commandDatabase.ExecuteNonQuery();
                
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
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();
                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        
                        if (id == reader.GetString(0))       // row[3] -> ID đọc từ bảng
                        {
                            //MessageBox.Show("UPDATE");
                            updateUser();
                            break;

                        }
                        else                    // CHƯA CÓ ID MÁY
                        {
                            //MessageBox.Show("INSERT");
                            insertData_realtime();
                            break;

                        }

                    }
                }
                else
                {
                    //Console.WriteLine("No rows found.");
                    insertData_realtime();
                }
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }


        private void insertData_realtime()
        {
            string query_insert = "INSERT INTO `save_realtime` (`Auto`, `TimePush`, `ID`, `S1`, `S2`, `On/Off`, `RFID`, `Barcode`, `Amp`, `Freg`, `MaxFreg`, `Counter`, `TimeFree`, `KWH`) VALUES ('" + auto + "','" + timepush + "','" + id + "','" + s1 + "','" + s2 + "','" + onoff + "','" + rfid + "'" +
                ",'" + barcode + "','" + amp + "','" + freg + "','" + maxfreg + "','" + counter + "','" + timefree + "','" + kwhs + "' )"; //auto, timepush, id, s1,s2,onoff,rfid,barcode,amp,freg,maxfreg,counter, timefree, kwh
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query_insert, databaseConnection);
            commandDatabase.CommandTimeout = 60;

            try
            {
                databaseConnection.Open();
                commandDatabase.ExecuteNonQuery();
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            try
            {
                if (m_sock == null || !m_sock.Connected)
                {
                    m_sock.Shutdown(SocketShutdown.Both);
                    m_sock.Close();
                    connected();
                }else
                    MessageBox.Show(this, "CONNECTED!");

            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR Connecting!");
            }
           
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            try
            {
                if (m_sock != null && m_sock.Connected)
                {
                    m_sock.Shutdown(SocketShutdown.Both);
                    m_sock.Close();
                }

                Application.Exit();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
            

        }

        private void machine_1_Click(object sender, EventArgs e)
        {
            try
            {
                timer1.Stop();

                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                
                this.Hide();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
            
        }
        private void machine_2_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_3_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_4_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_5_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_6_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_7_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_8_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
               // MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_9_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_10_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_11_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_12_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_13_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_14_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_15_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_16_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_17_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        private void machine_18_Click(object sender, EventArgs e)
        {
            try
            {
                m_sock.Shutdown(SocketShutdown.Both);
                m_sock.Close();
                Popup_Machine machine = new Popup_Machine();
                machine.Show();
                this.Hide();
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "ERROR!");
            }
        }

        
    }

}
