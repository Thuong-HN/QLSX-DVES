using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using COMExcel = Microsoft.Office.Interop.Excel;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using System.Threading;

namespace MqttForm
{
	public partial class Form1 : Form
	{
		
		private MqttClient localClient;
		private String ngay_1, ngay_2, ngay_3, ngay_4, ngay_5, ngay_6, ngay_7, ngay_8, ngay_9, ngay_10, ngay_11, ngay_12, ngay_13, ngay_14, ngay_15, ngay_16, ngay_17, ngay_18, ngay_19, ngay_20, ngay_21, ngay_22, ngay_23, ngay_24, ngay_25, ngay_26, ngay_27, ngay_28, ngay_29, ngay_30, ngay_31;
		private string monthss;
		private string yearss;
		//private string[] valueArray;
		//private String 
		//private int ngay1, ngay2, ngay3, ngay4, ngay5, ngay6, ngay7, ngay8, ngay9, ngay10, ngay11, ngay12, ngay13, ngay14, ngay15, ngay16, ngay17, ngay18, ngay19, ngay20, ngay21, ngay22, ngay23, ngay24, ngay25, ngay26, ngay27, ngay28, ngay29, ngay30, ngay31;
		public Form1()
		{
			InitializeComponent();
			
			try
			{
				//localClient.ProtocolVersion = MqttProtocolVersion.Version_3_1;
				localClient = new uPLibrary.Networking.M2Mqtt.MqttClient("10.11.15.201");
				string clientId = Guid.NewGuid().ToString();
				localClient.Connect(clientId);

				localClient.Subscribe(new String[] { "pub" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });

				//localClient.MqttMsgPublishReceived += Client_MqttMsgPublishReceived;

			}
			catch (Exception ex)
			{
				//Console.WriteLine("Connection Failed: " + ex.Message);
				MessageBox.Show("KHÔNG CÓ KẾT NỐI, KIỂM TRA KẾT NỐI MẠNG !");
			}

			
		}
		// ĐÓNG FILE EXCEL CÓ TÊN CỤ THỂ LẠI TRƯỚC KHI MỞ LẠI FILE
		

		private void KillSpecificExcelFileProcess()
		{
			var processes = from p in Process.GetProcessesByName("EXCEL")
							select p;

			foreach (var process in processes)
			{
				if (process.MainWindowTitle == "KH-SX.xlsx - Excel" || process.MainWindowTitle == "Microsoft Excel - KH-SX" || process.MainWindowTitle == "Microsoft Excel" || process.MainWindowTitle == "KH-SX - Excel")
					process.Kill();
			}
		}
		private void button1_Click(object sender, EventArgs e)
		{

			
			KillSpecificExcelFileProcess();
			// LẤY DỮ LIỆU TOÀN BẢNG EXCEL => LƯU VÀO TEXT
			
			try
			{
				
				DateTime realtime = DateTime.Now;
				monthss = (realtime.ToString("MM"));
				yearss = (realtime.ToString("yyyy"));
				Int32.TryParse(monthss, out int thangss);
				Int32.TryParse(yearss, out int namss);
				// LẤY DỮ LIỆU TỪ EXCEL GỬI ĐẾN RASPBERRY
				for (int i = 2019; i < 2030; i++)
				{
					for (int j = 1; j < 13; j++)
					{
						if (namss.Equals(i) && thangss.Equals(j) )
						{
							
							COMExcel.Application app = new COMExcel.Application();
							COMExcel.Workbook workbook = app.Workbooks.Open("D:/Ke Hoach San Xuat/" + yearss + "/KH-SX.xlsx");
							COMExcel.Worksheet xlWorksheet = (COMExcel.Worksheet)workbook.Sheets.get_Item(j);
							workbook.Activate();
							xlWorksheet.Activate();

							COMExcel.Range xlRange = xlWorksheet.UsedRange;
							
							object[,] valueArray = (object[,])xlRange.get_Value(COMExcel.XlRangeValueDataType.xlRangeValueDefault);
							for (int k = 4; k < 21; k++)
							{
								for (int l = 5; l < 66; l += 2)
								{
									if (valueArray[k, l] == null)
									{
										//MessageBox.Show("ĐÂY RỒI *********");
										valueArray[k, l] = 0;
									}
								}
							}
							try
							{

								// NẾU Ô EXCEL TRỐNG (NULL) THÌ SẼ BỊ LỖI KHI LƯU LẠI
							
								//MessageBox.Show(valueArray[4, 35].ToString());
								//localClient.Publish("sub", Encoding.UTF8.GetBytes("sanpham" + " " + valueArray[4, 1].ToString() + " " + valueArray[6, 1].ToString() + " " + valueArray[7, 1].ToString() + " " + valueArray[9, 1].ToString() + " " + valueArray[11, 1].ToString() + " " + valueArray[13, 1].ToString() + " " + valueArray[14, 1].ToString() + " " + valueArray[15, 1].ToString() + " " + valueArray[17, 1].ToString() + " " + valueArray[18, 1].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								//localClient.Publish("sub", Encoding.UTF8.GetBytes("loaisanpham" + " " + valueArray[4, 2].ToString() + " " + valueArray[5, 2].ToString() + " " + valueArray[6, 2].ToString() + " " + valueArray[7, 2].ToString() + " " + valueArray[8, 2].ToString() + " " + valueArray[9, 2].ToString() + " " + valueArray[10, 2].ToString() + " " + valueArray[11, 2].ToString() + " " + valueArray[12, 2].ToString() + " " + valueArray[13, 2].ToString() + " " + valueArray[14, 2].ToString() + " " + valueArray[15, 2].ToString() + " " + valueArray[16, 2].ToString() + " " + valueArray[17, 2].ToString() + " " + valueArray[18, 2].ToString() + " " + valueArray[19, 2].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);

								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_1" + " " + valueArray[4, 5].ToString() + " " + valueArray[5, 5].ToString() + " " + valueArray[6, 5].ToString() + " " + valueArray[7, 5].ToString() + " " + valueArray[8, 5].ToString() + " " + valueArray[9, 5].ToString() + " " + valueArray[10, 5].ToString() + " " + valueArray[11, 5].ToString() + " " + valueArray[12, 5].ToString() + " " + valueArray[13, 5].ToString() + " " + valueArray[14, 5].ToString() + " " + valueArray[15, 5].ToString() + " " + valueArray[16, 5].ToString() + " " + valueArray[17, 5].ToString() + " " + valueArray[18, 5].ToString() + " " + valueArray[19, 5].ToString() + " " + valueArray[20, 5].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_2" + " " + valueArray[4, 7].ToString() + " " + valueArray[5, 7].ToString() + " " + valueArray[6, 7].ToString() + " " + valueArray[7, 7].ToString() + " " + valueArray[8, 7].ToString() + " " + valueArray[9, 7].ToString() + " " + valueArray[10, 7].ToString() + " " + valueArray[11, 7].ToString() + " " + valueArray[12, 7].ToString() + " " + valueArray[13, 7].ToString() + " " + valueArray[14, 7].ToString() + " " + valueArray[15, 7].ToString() + " " + valueArray[16, 7].ToString() + " " + valueArray[17, 7].ToString() + " " + valueArray[18, 7].ToString() + " " + valueArray[19, 7].ToString() + " " + valueArray[20, 7].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_3" + " " + valueArray[4, 9].ToString() + " " + valueArray[5, 9].ToString() + " " + valueArray[6, 9].ToString() + " " + valueArray[7, 9].ToString() + " " + valueArray[8, 9].ToString() + " " + valueArray[9, 9].ToString() + " " + valueArray[10, 9].ToString() + " " + valueArray[11, 9].ToString() + " " + valueArray[12, 9].ToString() + " " + valueArray[13, 9].ToString() + " " + valueArray[14, 9].ToString() + " " + valueArray[15, 9].ToString() + " " + valueArray[16, 9].ToString() + " " + valueArray[17, 9].ToString() + " " + valueArray[18, 9].ToString() + " " + valueArray[19, 9].ToString() + " " + valueArray[20, 9].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_4" + " " + valueArray[4, 11].ToString() + " " + valueArray[5, 11].ToString() + " " + valueArray[6, 11].ToString() + " " + valueArray[7, 11].ToString() + " " + valueArray[8, 11].ToString() + " " + valueArray[9, 11].ToString() + " " + valueArray[10, 11].ToString() + " " + valueArray[11, 11].ToString() + " " + valueArray[12, 11].ToString() + " " + valueArray[13, 11].ToString() + " " + valueArray[14, 11].ToString() + " " + valueArray[15, 11].ToString() + " " + valueArray[16, 11].ToString() + " " + valueArray[17, 11].ToString() + " " + valueArray[18, 11].ToString() + " " + valueArray[19, 11].ToString() + " " + valueArray[20, 11].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_5" + " " + valueArray[4, 13].ToString() + " " + valueArray[5, 13].ToString() + " " + valueArray[6, 13].ToString() + " " + valueArray[7, 13].ToString() + " " + valueArray[8, 13].ToString() + " " + valueArray[9, 13].ToString() + " " + valueArray[10, 13].ToString() + " " + valueArray[11, 13].ToString() + " " + valueArray[12, 13].ToString() + " " + valueArray[13, 13].ToString() + " " + valueArray[14, 13].ToString() + " " + valueArray[15, 13].ToString() + " " + valueArray[16, 13].ToString() + " " + valueArray[17, 13].ToString() + " " + valueArray[18, 13].ToString() + " " + valueArray[19, 13].ToString() + " " + valueArray[20, 13].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_6" + " " + valueArray[4, 15].ToString() + " " + valueArray[5, 15].ToString() + " " + valueArray[6, 15].ToString() + " " + valueArray[7, 15].ToString() + " " + valueArray[8, 15].ToString() + " " + valueArray[9, 15].ToString() + " " + valueArray[10, 15].ToString() + " " + valueArray[11, 15].ToString() + " " + valueArray[12, 15].ToString() + " " + valueArray[13, 15].ToString() + " " + valueArray[14, 15].ToString() + " " + valueArray[15, 15].ToString() + " " + valueArray[16, 15].ToString() + " " + valueArray[17, 15].ToString() + " " + valueArray[18, 15].ToString() + " " + valueArray[19, 15].ToString() + " " + valueArray[20, 15].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_7" + " " + valueArray[4, 17].ToString() + " " + valueArray[5, 17].ToString() + " " + valueArray[6, 17].ToString() + " " + valueArray[7, 17].ToString() + " " + valueArray[8, 17].ToString() + " " + valueArray[9, 17].ToString() + " " + valueArray[10, 17].ToString() + " " + valueArray[11, 17].ToString() + " " + valueArray[12, 17].ToString() + " " + valueArray[13, 17].ToString() + " " + valueArray[14, 17].ToString() + " " + valueArray[15, 17].ToString() + " " + valueArray[16, 17].ToString() + " " + valueArray[17, 17].ToString() + " " + valueArray[18, 17].ToString() + " " + valueArray[19, 17].ToString() + " " + valueArray[20, 17].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_8" + " " + valueArray[4, 19].ToString() + " " + valueArray[5, 19].ToString() + " " + valueArray[6, 19].ToString() + " " + valueArray[7, 19].ToString() + " " + valueArray[8, 19].ToString() + " " + valueArray[9, 19].ToString() + " " + valueArray[10, 19].ToString() + " " + valueArray[11, 19].ToString() + " " + valueArray[12, 19].ToString() + " " + valueArray[13, 19].ToString() + " " + valueArray[14, 19].ToString() + " " + valueArray[15, 19].ToString() + " " + valueArray[16, 19].ToString() + " " + valueArray[17, 19].ToString() + " " + valueArray[18, 19].ToString() + " " + valueArray[19, 19].ToString() + " " + valueArray[20, 19].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_9" + " " + valueArray[4, 21].ToString() + " " + valueArray[5, 21].ToString() + " " + valueArray[6, 21].ToString() + " " + valueArray[7, 21].ToString() + " " + valueArray[8, 21].ToString() + " " + valueArray[9, 21].ToString() + " " + valueArray[10, 21].ToString() + " " + valueArray[11, 21].ToString() + " " + valueArray[12, 21].ToString() + " " + valueArray[13, 21].ToString() + " " + valueArray[14, 21].ToString() + " " + valueArray[15, 21].ToString() + " " + valueArray[16, 21].ToString() + " " + valueArray[17, 21].ToString() + " " + valueArray[18, 21].ToString() + " " + valueArray[19, 21].ToString() + " " + valueArray[20, 21].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_10" + " " + valueArray[4, 23].ToString() + " " + valueArray[5, 23].ToString() + " " + valueArray[6, 23].ToString() + " " + valueArray[7, 23].ToString() + " " + valueArray[8, 23].ToString() + " " + valueArray[9, 23].ToString() + " " + valueArray[10, 23].ToString() + " " + valueArray[11, 23].ToString() + " " + valueArray[12, 23].ToString() + " " + valueArray[13, 23].ToString() + " " + valueArray[14, 23].ToString() + " " + valueArray[15, 23].ToString() + " " + valueArray[16, 23].ToString() + " " + valueArray[17, 23].ToString() + " " + valueArray[18, 23].ToString() + " " + valueArray[19, 23].ToString() + " " + valueArray[20, 23].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_11" + " " + valueArray[4, 25].ToString() + " " + valueArray[5, 25].ToString() + " " + valueArray[6, 25].ToString() + " " + valueArray[7, 25].ToString() + " " + valueArray[8, 25].ToString() + " " + valueArray[9, 25].ToString() + " " + valueArray[10, 25].ToString() + " " + valueArray[11, 25].ToString() + " " + valueArray[12, 25].ToString() + " " + valueArray[13, 25].ToString() + " " + valueArray[14, 25].ToString() + " " + valueArray[15, 25].ToString() + " " + valueArray[16, 25].ToString() + " " + valueArray[17, 25].ToString() + " " + valueArray[18, 25].ToString() + " " + valueArray[19, 25].ToString() + " " + valueArray[20, 25].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_12" + " " + valueArray[4, 27].ToString() + " " + valueArray[5, 27].ToString() + " " + valueArray[6, 27].ToString() + " " + valueArray[7, 27].ToString() + " " + valueArray[8, 27].ToString() + " " + valueArray[9, 27].ToString() + " " + valueArray[10, 27].ToString() + " " + valueArray[11, 27].ToString() + " " + valueArray[12, 27].ToString() + " " + valueArray[13, 27].ToString() + " " + valueArray[14, 27].ToString() + " " + valueArray[15, 27].ToString() + " " + valueArray[16, 27].ToString() + " " + valueArray[17, 27].ToString() + " " + valueArray[18, 27].ToString() + " " + valueArray[19, 27].ToString() + " " + valueArray[20, 27].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);

								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_13" + " " + valueArray[4, 29].ToString() + " " + valueArray[5, 29].ToString() + " " + valueArray[6, 29].ToString() + " " + valueArray[7, 29].ToString() + " " + valueArray[8, 29].ToString() + " " + valueArray[9, 29].ToString() + " " + valueArray[10, 29].ToString() + " " + valueArray[11, 29].ToString() + " " + valueArray[12, 29].ToString() + " " + valueArray[13, 29].ToString() + " " + valueArray[14, 29].ToString() + " " + valueArray[15, 29].ToString() + " " + valueArray[16, 29].ToString() + " " + valueArray[17, 29].ToString() + " " + valueArray[18, 29].ToString() + " " + valueArray[19, 29].ToString() + " " + valueArray[20, 29].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_14" + " " + valueArray[4, 31].ToString() + " " + valueArray[5, 31].ToString() + " " + valueArray[6, 31].ToString() + " " + valueArray[7, 31].ToString() + " " + valueArray[8, 31].ToString() + " " + valueArray[9, 31].ToString() + " " + valueArray[10, 31].ToString() + " " + valueArray[11, 31].ToString() + " " + valueArray[12, 31].ToString() + " " + valueArray[13, 31].ToString() + " " + valueArray[14, 31].ToString() + " " + valueArray[15, 31].ToString() + " " + valueArray[16, 31].ToString() + " " + valueArray[17, 31].ToString() + " " + valueArray[18, 31].ToString() + " " + valueArray[19, 31].ToString() + " " + valueArray[20, 31].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_15" + " " + valueArray[4, 33].ToString() + " " + valueArray[5, 33].ToString() + " " + valueArray[6, 33].ToString() + " " + valueArray[7, 33].ToString() + " " + valueArray[8, 33].ToString() + " " + valueArray[9, 33].ToString() + " " + valueArray[10, 33].ToString() + " " + valueArray[11, 33].ToString() + " " + valueArray[12, 33].ToString() + " " + valueArray[13, 33].ToString() + " " + valueArray[14, 33].ToString() + " " + valueArray[15, 33].ToString() + " " + valueArray[16, 33].ToString() + " " + valueArray[17, 33].ToString() + " " + valueArray[18, 33].ToString() + " " + valueArray[19, 33].ToString() + " " + valueArray[20, 33].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								//Thread.Sleep(100);


								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_16" + " " + valueArray[4, 35].ToString() + " " + valueArray[5, 35].ToString() + " " + valueArray[6, 35].ToString() + " " + valueArray[7, 35].ToString() + " " + valueArray[8, 35].ToString() + " " + valueArray[9, 35].ToString() + " " + valueArray[10, 35].ToString() + " " + valueArray[11, 35].ToString() + " " + valueArray[12, 35].ToString() + " " + valueArray[13, 35].ToString() + " " + valueArray[14, 35].ToString() + " " + valueArray[15, 35].ToString() + " " + valueArray[16, 35].ToString() + " " + valueArray[17, 35].ToString() + " " + valueArray[18, 35].ToString() + " " + valueArray[19, 35].ToString() + " " + valueArray[20, 35].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_17" + " " + valueArray[4, 37].ToString() + " " + valueArray[5, 37].ToString() + " " + valueArray[6, 37].ToString() + " " + valueArray[7, 37].ToString() + " " + valueArray[8, 37].ToString() + " " + valueArray[9, 37].ToString() + " " + valueArray[10, 37].ToString() + " " + valueArray[11, 37].ToString() + " " + valueArray[12, 37].ToString() + " " + valueArray[13, 37].ToString() + " " + valueArray[14, 37].ToString() + " " + valueArray[15, 37].ToString() + " " + valueArray[16, 37].ToString() + " " + valueArray[17, 37].ToString() + " " + valueArray[18, 37].ToString() + " " + valueArray[19, 37].ToString() + " " + valueArray[20, 37].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_18" + " " + valueArray[4, 39].ToString() + " " + valueArray[5, 39].ToString() + " " + valueArray[6, 39].ToString() + " " + valueArray[7, 39].ToString() + " " + valueArray[8, 39].ToString() + " " + valueArray[9, 39].ToString() + " " + valueArray[10, 39].ToString() + " " + valueArray[11, 39].ToString() + " " + valueArray[12, 39].ToString() + " " + valueArray[13, 39].ToString() + " " + valueArray[14, 39].ToString() + " " + valueArray[15, 39].ToString() + " " + valueArray[16, 39].ToString() + " " + valueArray[17, 39].ToString() + " " + valueArray[18, 39].ToString() + " " + valueArray[19, 39].ToString() + " " + valueArray[20, 39].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_19" + " " + valueArray[4, 41].ToString() + " " + valueArray[5, 41].ToString() + " " + valueArray[6, 41].ToString() + " " + valueArray[7, 41].ToString() + " " + valueArray[8, 41].ToString() + " " + valueArray[9, 41].ToString() + " " + valueArray[10, 41].ToString() + " " + valueArray[11, 41].ToString() + " " + valueArray[12, 41].ToString() + " " + valueArray[13, 41].ToString() + " " + valueArray[14, 41].ToString() + " " + valueArray[15, 41].ToString() + " " + valueArray[16, 41].ToString() + " " + valueArray[17, 41].ToString() + " " + valueArray[18, 41].ToString() + " " + valueArray[19, 41].ToString() + " " + valueArray[20, 41].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_20" + " " + valueArray[4, 43].ToString() + " " + valueArray[5, 43].ToString() + " " + valueArray[6, 43].ToString() + " " + valueArray[7, 43].ToString() + " " + valueArray[8, 43].ToString() + " " + valueArray[9, 43].ToString() + " " + valueArray[10, 43].ToString() + " " + valueArray[11, 43].ToString() + " " + valueArray[12, 43].ToString() + " " + valueArray[13, 43].ToString() + " " + valueArray[14, 43].ToString() + " " + valueArray[15, 43].ToString() + " " + valueArray[16, 43].ToString() + " " + valueArray[17, 43].ToString() + " " + valueArray[18, 43].ToString() + " " + valueArray[19, 43].ToString() + " " + valueArray[20, 43].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_21" + " " + valueArray[4, 45].ToString() + " " + valueArray[5, 45].ToString() + " " + valueArray[6, 45].ToString() + " " + valueArray[7, 45].ToString() + " " + valueArray[8, 45].ToString() + " " + valueArray[9, 45].ToString() + " " + valueArray[10, 45].ToString() + " " + valueArray[11, 45].ToString() + " " + valueArray[12, 45].ToString() + " " + valueArray[13, 45].ToString() + " " + valueArray[14, 45].ToString() + " " + valueArray[15, 45].ToString() + " " + valueArray[16, 45].ToString() + " " + valueArray[17, 45].ToString() + " " + valueArray[18, 45].ToString() + " " + valueArray[19, 45].ToString() + " " + valueArray[20, 45].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_22" + " " + valueArray[4, 47].ToString() + " " + valueArray[5, 47].ToString() + " " + valueArray[6, 47].ToString() + " " + valueArray[7, 47].ToString() + " " + valueArray[8, 47].ToString() + " " + valueArray[9, 47].ToString() + " " + valueArray[10, 47].ToString() + " " + valueArray[11, 47].ToString() + " " + valueArray[12, 47].ToString() + " " + valueArray[13, 47].ToString() + " " + valueArray[14, 47].ToString() + " " + valueArray[15, 47].ToString() + " " + valueArray[16, 47].ToString() + " " + valueArray[17, 47].ToString() + " " + valueArray[18, 47].ToString() + " " + valueArray[19, 47].ToString() + " " + valueArray[20, 47].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_23" + " " + valueArray[4, 49].ToString() + " " + valueArray[5, 49].ToString() + " " + valueArray[6, 49].ToString() + " " + valueArray[7, 49].ToString() + " " + valueArray[8, 49].ToString() + " " + valueArray[9, 49].ToString() + " " + valueArray[10, 49].ToString() + " " + valueArray[11, 49].ToString() + " " + valueArray[12, 49].ToString() + " " + valueArray[13, 49].ToString() + " " + valueArray[14, 49].ToString() + " " + valueArray[15, 49].ToString() + " " + valueArray[16, 49].ToString() + " " + valueArray[17, 49].ToString() + " " + valueArray[18, 49].ToString() + " " + valueArray[19, 49].ToString() + " " + valueArray[20, 49].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);

								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_24" + " " + valueArray[4, 51].ToString() + " " + valueArray[5, 51].ToString() + " " + valueArray[6, 51].ToString() + " " + valueArray[7, 51].ToString() + " " + valueArray[8, 51].ToString() + " " + valueArray[9, 51].ToString() + " " + valueArray[10, 51].ToString() + " " + valueArray[11, 51].ToString() + " " + valueArray[12, 51].ToString() + " " + valueArray[13, 51].ToString() + " " + valueArray[14, 51].ToString() + " " + valueArray[15, 51].ToString() + " " + valueArray[16, 51].ToString() + " " + valueArray[17, 51].ToString() + " " + valueArray[18, 51].ToString() + " " + valueArray[19, 51].ToString() + " " + valueArray[20, 51].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_25" + " " + valueArray[4, 53].ToString() + " " + valueArray[5, 53].ToString() + " " + valueArray[6, 53].ToString() + " " + valueArray[7, 53].ToString() + " " + valueArray[8, 53].ToString() + " " + valueArray[9, 53].ToString() + " " + valueArray[10, 53].ToString() + " " + valueArray[11, 53].ToString() + " " + valueArray[12, 53].ToString() + " " + valueArray[13, 53].ToString() + " " + valueArray[14, 53].ToString() + " " + valueArray[15, 53].ToString() + " " + valueArray[16, 53].ToString() + " " + valueArray[17, 53].ToString() + " " + valueArray[18, 53].ToString() + " " + valueArray[19, 53].ToString() + " " + valueArray[20, 53].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_26" + " " + valueArray[4, 55].ToString() + " " + valueArray[5, 55].ToString() + " " + valueArray[6, 55].ToString() + " " + valueArray[7, 55].ToString() + " " + valueArray[8, 55].ToString() + " " + valueArray[9, 55].ToString() + " " + valueArray[10, 55].ToString() + " " + valueArray[11, 55].ToString() + " " + valueArray[12, 55].ToString() + " " + valueArray[13, 55].ToString() + " " + valueArray[14, 55].ToString() + " " + valueArray[15, 55].ToString() + " " + valueArray[16, 55].ToString() + " " + valueArray[17, 55].ToString() + " " + valueArray[18, 55].ToString() + " " + valueArray[19, 55].ToString() + " " + valueArray[20, 55].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_27" + " " + valueArray[4, 57].ToString() + " " + valueArray[5, 57].ToString() + " " + valueArray[6, 57].ToString() + " " + valueArray[7, 57].ToString() + " " + valueArray[8, 57].ToString() + " " + valueArray[9, 57].ToString() + " " + valueArray[10, 57].ToString() + " " + valueArray[11, 57].ToString() + " " + valueArray[12, 57].ToString() + " " + valueArray[13, 57].ToString() + " " + valueArray[14, 57].ToString() + " " + valueArray[15, 57].ToString() + " " + valueArray[16, 57].ToString() + " " + valueArray[17, 57].ToString() + " " + valueArray[18, 57].ToString() + " " + valueArray[19, 57].ToString() + " " + valueArray[20, 57].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_28" + " " + valueArray[4, 59].ToString() + " " + valueArray[5, 59].ToString() + " " + valueArray[6, 59].ToString() + " " + valueArray[7, 59].ToString() + " " + valueArray[8, 59].ToString() + " " + valueArray[9, 59].ToString() + " " + valueArray[10, 59].ToString() + " " + valueArray[11, 59].ToString() + " " + valueArray[12, 59].ToString() + " " + valueArray[13, 59].ToString() + " " + valueArray[14, 59].ToString() + " " + valueArray[15, 59].ToString() + " " + valueArray[16, 59].ToString() + " " + valueArray[17, 59].ToString() + " " + valueArray[18, 59].ToString() + " " + valueArray[19, 59].ToString() + " " + valueArray[20, 59].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_29" + " " + valueArray[4, 61].ToString() + " " + valueArray[5, 61].ToString() + " " + valueArray[6, 61].ToString() + " " + valueArray[7, 61].ToString() + " " + valueArray[8, 61].ToString() + " " + valueArray[9, 61].ToString() + " " + valueArray[10, 61].ToString() + " " + valueArray[11, 61].ToString() + " " + valueArray[12, 61].ToString() + " " + valueArray[13, 61].ToString() + " " + valueArray[14, 61].ToString() + " " + valueArray[15, 61].ToString() + " " + valueArray[16, 61].ToString() + " " + valueArray[17, 61].ToString() + " " + valueArray[18, 61].ToString() + " " + valueArray[19, 61].ToString() + " " + valueArray[20, 61].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_30" + " " + valueArray[4, 63].ToString() + " " + valueArray[5, 63].ToString() + " " + valueArray[6, 63].ToString() + " " + valueArray[7, 63].ToString() + " " + valueArray[8, 63].ToString() + " " + valueArray[9, 63].ToString() + " " + valueArray[10, 63].ToString() + " " + valueArray[11, 63].ToString() + " " + valueArray[12, 63].ToString() + " " + valueArray[13, 63].ToString() + " " + valueArray[14, 63].ToString() + " " + valueArray[15, 63].ToString() + " " + valueArray[16, 63].ToString() + " " + valueArray[17, 63].ToString() + " " + valueArray[18, 63].ToString() + " " + valueArray[19, 63].ToString() + " " + valueArray[20, 63].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
								localClient.Publish("sub", Encoding.UTF8.GetBytes("khngay_31" + " " + valueArray[4, 65].ToString() + " " + valueArray[5, 65].ToString() + " " + valueArray[6, 65].ToString() + " " + valueArray[7, 65].ToString() + " " + valueArray[8, 65].ToString() + " " + valueArray[9, 65].ToString() + " " + valueArray[10, 65].ToString() + " " + valueArray[11, 65].ToString() + " " + valueArray[12, 65].ToString() + " " + valueArray[13, 65].ToString() + " " + valueArray[14, 65].ToString() + " " + valueArray[15, 65].ToString() + " " + valueArray[16, 65].ToString() + " " + valueArray[17, 65].ToString() + " " + valueArray[18, 65].ToString() + " " + valueArray[19, 65].ToString() + " " + valueArray[20, 65].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);

								//localClient.Publish("sub", Encoding.UTF8.GetBytes("tong_kehoach" + " " + valueArray[4, 67].ToString() + " " + valueArray[5, 67].ToString() + " " + valueArray[6, 67].ToString() + " " + valueArray[7, 67].ToString() + " " + valueArray[8, 67].ToString() + " " + valueArray[9, 67].ToString() + " " + valueArray[10, 67].ToString() + " " + valueArray[11, 67].ToString() + " " + valueArray[12, 67].ToString() + " " + valueArray[13, 65].ToString() + " " + valueArray[14, 67].ToString() + " " + valueArray[15, 67].ToString() + " " + valueArray[16, 67].ToString() + " " + valueArray[17, 67].ToString() + " " + valueArray[18, 67].ToString() + " " + valueArray[19, 67].ToString() + " " + valueArray[20, 67].ToString()), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);



								app.DisplayAlerts = false;
								workbook.Close(true);
								app.Quit();
								System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook);
								System.Runtime.InteropServices.Marshal.ReleaseComObject(app);
								System.Runtime.InteropServices.Marshal.ReleaseComObject(xlWorksheet);
								KillSpecificExcelFileProcess();
								// TÊN SẢN PHẨM
								//if (localClient.IsConnected)
								//{

								/*

								localClient.Publish("sub", Encoding.UTF8.GetBytes("sanpham" + " " + valueArray[4, 1].ToString() + " " + valueArray[6, 1].ToString() + " " + valueArray[7, 1].ToString() + " " + valueArray[9, 1].ToString() + " " + valueArray[11, 1].ToString() + " " + valueArray[13, 1].ToString() + " " + valueArray[14, 1].ToString() + " " + valueArray[15, 1].ToString() + " " + valueArray[17, 1].ToString() + " " + valueArray[18, 1].ToString() + " " + "loaisanpham" + " " + valueArray[4, 2].ToString() + " " + valueArray[5, 2].ToString() + " " + valueArray[6, 2].ToString() + " " + valueArray[7, 2].ToString() + " " + valueArray[8, 2].ToString() + " " + valueArray[9, 2].ToString() 
									+ " " + valueArray[10, 2].ToString() + " " + valueArray[11, 2].ToString() + " " + valueArray[12, 2].ToString() + " " + valueArray[13, 2].ToString() + " " + valueArray[14, 2].ToString() + " " + valueArray[15, 2].ToString() + " " + valueArray[16, 2].ToString() + " " + valueArray[17, 2].ToString() + " " + valueArray[18, 2].ToString() + " " + valueArray[19, 2].ToString()
									+ " " + "tong_kehoach" + " " + valueArray[4, 67].ToString() + " " + valueArray[5, 67].ToString() + " " + valueArray[6, 67].ToString() + " " + valueArray[7, 67].ToString() + " " + valueArray[8, 67].ToString() + " " + valueArray[9, 67].ToString() + " " + valueArray[10, 67].ToString() + " " + valueArray[11, 67].ToString() + " " + valueArray[12, 67].ToString() + " " + valueArray[13, 65].ToString() + " " + valueArray[14, 67].ToString() + " " + valueArray[15, 67].ToString() + " " + valueArray[16, 67].ToString() + " " + valueArray[17, 67].ToString() + " " + valueArray[18, 67].ToString() + " " + valueArray[19, 67].ToString() + " " + valueArray[20, 67].ToString()



									), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);

								*/

								// KẾ HOẠCH TỪ NGÀY 1 -> NGÀY 15




								//}

							}
							catch (Exception ex)
							{
								MessageBox.Show("Lỗi file excel, vui lòng kiểm tra đường dẫn!");
								workbook.Close(true);
								app.Quit();
								System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook);
								System.Runtime.InteropServices.Marshal.ReleaseComObject(app);
								System.Runtime.InteropServices.Marshal.ReleaseComObject(xlWorksheet);
								KillSpecificExcelFileProcess();
							}

						}
					}
				}
				
				
			}
			
			catch (Exception ex)
			{

				MessageBox.Show("LỖI FILE!");
				KillSpecificExcelFileProcess();
			}


			
			
			this.Close();
			Chuongtrinhchinh ctc = new Chuongtrinhchinh();
			ctc.Show();
		}

		private void QUAY_LAI_Click(object sender, EventArgs e)
		{
			KillSpecificExcelFileProcess();
			this.Close();
			Chuongtrinhchinh ctc = new Chuongtrinhchinh();
			ctc.Show();

		}
	}
}
