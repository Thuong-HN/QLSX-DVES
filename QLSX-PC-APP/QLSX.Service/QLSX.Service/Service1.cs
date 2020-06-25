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
        private int kwh;
        private Socket m_sock;                      
        private byte[] m_byBuff = new byte[1024];    

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
            try
            {
                if (m_sock == null || !m_sock.Connected)
                {
                    WriteToFile("Service is running... DISCONNECT: " + DateTime.Now);
                    connected();
                }
                else
                {
                    SenData();
                    WriteToFile("Service is running... CONNECTED: " + DateTime.Now);
                }
            }
            catch (Exception ex)
            {
                throw;
            }
            
        }


        private void connected()
        {
           
            try
            {
                if (m_sock != null && m_sock.Connected)
                {
                    m_sock.Shutdown(SocketShutdown.Both);
                    //System.Threading.Thread.Sleep(10);
                    m_sock.Close(); 
                }
                m_sock = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                IPEndPoint epServer = new IPEndPoint(IPAddress.Parse("192.168.2.244"), 80);
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
            Socket sock = (Socket)ar.AsyncState;
            try
            {
                if (sock.Connected)
                    SetupRecieveCallback(sock);
                else
                    connected();
                    //MessageBox.Show(this, "Unable to connect to remote machine", "Connect Failed!");
            }
            catch (Exception ex)
            {
                //MessageBox.Show(this, ex.Message, "Unusual error during Connect!");
            }
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
                    string[] tokens = sRecieved.Split(',');
                    auto = tokens[0]; timepush = tokens[1];id = tokens[2];
                    if (!auto.Equals('1'))
                    {
                        insertData();
                    }
                    
                    SetupRecieveCallback(sock);
                }
                else
                {
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
        private void SenData()
        {


            try
            {
                if (m_sock == null || !m_sock.Connected)
                {
                    return;
                }

                Byte[] byteDateLine = Encoding.ASCII.GetBytes("OK".ToCharArray());
                m_sock.Send(byteDateLine, byteDateLine.Length, 0);
                
            }
            catch (Exception ex)
            {
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





        private void insertData()
        {
            string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=qlsx_dves;";
            string query = "INSERT INTO save_data(`Auto`, `Time Push`, `ID`) VALUES ('" + auto + "','" + timepush + "','" + id + "')";
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
               
            }
        }
        private void updateUser()
        {
            string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=qlsx_dves;";
            string query = "UPDATE `user` SET `first_name`='Willy',`last_name`='Wonka',`address`='Chocolate factory' WHERE id = 1";

            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            commandDatabase.CommandTimeout = 60;
            MySqlDataReader reader;

            try
            {
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
               
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
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
               
            }
        }


    }
}
