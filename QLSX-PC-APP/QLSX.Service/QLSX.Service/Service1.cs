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
using System.Threading;
using System.Threading.Tasks;
using System.Timers;
using MySql.Data.MySqlClient;


namespace QLSX.Service
{
    public partial class Service1 : ServiceBase
    {
        private static System.Timers.Timer timer;
        private string connectionString = "datasource=127.0.0.1;port=3306;username=root;password=;database=qlsx_dves;";
        private Socket m_sock;
        private byte[] m_byBuff = new byte[1024];
        private string auto, timepush, id, s1, s2, onoff, rfid, barcode, amp, freg, maxfreg, counter, timefree, kwh;


        public Service1()
        {
            InitializeComponent();
            timer = new System.Timers.Timer();
            connected();

        }

        protected override void OnStart(string[] args)
        {
            WriteToFile("Service is start... AT: " + DateTime.Now);
            timer.Elapsed += new ElapsedEventHandler(OnElapsedTime);
            timer.Interval = 2000; //number in milisecinds  
            timer.Enabled = true;
        }

        protected override void OnStop()
        {
            WriteToFile("Service is stopped AT:  " + DateTime.Now);
            WriteToFile("----------------------------------------");
        }

        private void OnElapsedTime(object source, ElapsedEventArgs e)
        {
            try
            {
                if (!IsSocketConnected(m_sock) || m_sock == null)
                {
                    WriteToFile("Service is running... DISCONNECT: " + DateTime.Now);
                    connected();
                }
                else
                {
                    WriteToFile("Service is running... CONNECTED: " + DateTime.Now);
                    SenData();
                }

            }
            catch (Exception ex)
            {

            }

        }
        static bool IsSocketConnected(Socket s)
        {
            return !((s.Poll(1000, SelectMode.SelectRead) && (s.Available == 0)) || !s.Connected);
        }
        private void connected()
        {

            try
            {
                if (m_sock != null && !m_sock.Connected)
                {
                    m_sock.Shutdown(SocketShutdown.Both);
                    System.Threading.Thread.Sleep(2);
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
                    auto = tokens[0]; timepush = tokens[1]; id = tokens[2]; s1 = tokens[3]; s2 = tokens[4]; onoff = tokens[5]; rfid = tokens[6]; barcode = tokens[7]; amp = tokens[8]; freg = tokens[9];
                    maxfreg = tokens[10]; counter = tokens[11]; timefree = tokens[12]; kwh = tokens[13];
                    if (auto != "1")
                    {
                        insertData_saveDB();
                    }
                    Thread t = new Thread(getData);
                    t.Start();
                    SetupRecieveCallback(sock);
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

                Byte[] byteDateLine = Encoding.ASCII.GetBytes("SERVICES".ToCharArray());
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
        private void getData()
        {
            string query = "SELECT ID FROM save_realtime ";
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

                        if (id == reader.GetString(0))          // row[0] -> ID đọc từ bảng
                        {
                            updateData_realtime();
                            break;

                        }
                        else                                    // CHƯA CÓ ID MÁY
                        {
                            insertData_realtime();
                            break;

                        }

                    }

                }
                else
                {
                    insertData_realtime();
                }
                databaseConnection.Close();

            }
            catch (Exception ex)
            {

            }
        }
        private void updateData_realtime()
        {
            string query_update = "UPDATE `save_realtime` SET `Auto` = '" + auto + "', `TimePush` = '" + timepush + "', `ID`='" + id + "', `S1`='" + s1 + "', `S2`='" + s2 + "', `On/Off`='" + onoff + "', `RFID`='" + rfid + "', `Barcode`='" + barcode + "', `Amp`='" + amp + "', `Freg`='" + freg + "', `MaxFreg`='" + maxfreg + "', `Counter`='" + counter + "', `TimeFree`='" + timefree + "', `KWH`='" + kwh + "' WHERE `ID` = '" + id + "' ";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query_update, databaseConnection);
            commandDatabase.CommandTimeout = 60;

            try
            {
                databaseConnection.Open();
                commandDatabase.ExecuteNonQuery();
                databaseConnection.Close();
            }
            catch (Exception ex)
            {

            }
        }
        private void insertData_realtime()
        {
            string query_insert = "INSERT INTO save_realtime(`Auto`, `TimePush`, `ID`, `S1`, `S2`, `On/Off`, `RFID`, `Barcode`, `Amp`, `Freg`, `MaxFreg`, `Counter`, `TimeFree`, `KWH`) VALUES ('" + auto + "','" + timepush + "','" + id + "','" + s1 + "','" + s2 + "','" + onoff + "','" + rfid + "'" +
                ",'" + barcode + "','" + amp + "','" + freg + "','" + maxfreg + "','" + counter + "','" + timefree + "','" + kwh + "' )"; //auto, timepush, id, s1,s2,onoff,rfid,barcode,amp,freg,maxfreg,counter, timefree, kwh
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

            }
        }
        private void insertData_saveDB()
        {
            string query_insertDB = "INSERT INTO save_data(`Auto`, `TimePush`, `ID`, `S1`, `S2`, `On/Off`, `RFID`, `Barcode`, `Amp`, `Freg`, `MaxFreg`, `Counter`, `TimeFree`, `KWH`) VALUES ('" + auto + "','" + timepush + "','" + id + "','" + s1 + "','" + s2 + "','" + onoff + "','" + rfid + "'" +
                ",'" + barcode + "','" + amp + "','" + freg + "','" + maxfreg + "','" + counter + "','" + timefree + "','" + kwh + "' )"; //auto, timepush, id, s1,s2,onoff,rfid,barcode,amp,freg,maxfreg,counter, timefree, kwh
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query_insertDB, databaseConnection);
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

        


    }
}
