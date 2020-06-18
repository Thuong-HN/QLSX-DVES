using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using uPLibrary.Networking.M2Mqtt;
using System.Windows.Forms;
using uPLibrary.Networking.M2Mqtt.Messages;
using COMExcel = Microsoft.Office.Interop.Excel;
using System.Diagnostics;
using Microsoft.Office.Interop.Excel;
using System.Reflection;
using System.ComponentModel;

namespace MqttForm
{
	public partial class xuatdulieu : Form
	{
		
		private int start = 0, repeat = 0;
		private MqttClient localClient;
		string message = "";
		private int ngayss,thangss,namss;
		private string[] mestmp,ngaysave;
		private string thang,ngay1;
		private string nam;
		
		public xuatdulieu()
		{
			InitializeComponent();
			try
			{
				pictureBox1.Visible = false;
				label2.Visible = false;
				label2.Parent = pictureBox1;
				//localClient.ProtocolVersion = MqttProtocolVersion.Version_3_1;
				localClient = new uPLibrary.Networking.M2Mqtt.MqttClient("10.11.15.201");
				string clientId = Guid.NewGuid().ToString();
				localClient.Connect(clientId);

				localClient.Subscribe(new String[] { "pub" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
				
				localClient.MqttMsgPublishReceived += Client_MqttMsgPublishReceived;

			}
			catch (Exception ex)
			{
				//Console.WriteLine("Connection Failed: " + ex.Message);
				MessageBox.Show("KHÔNG CÓ KẾT NỐI, KIỂM TRA KẾT NỐI MẠNG !");
			}
		}
		
		
		private void ngaythangnam_DateChanged(object sender, DateRangeEventArgs e)
		{
			KillSpecificExcelFileProcess();
			//MessageBox.Show("Dates Selected from :" + (ngaythangnam.SelectionRange.Start + " to " + ngaythangnam.SelectionRange.End));
			ngay.Text = ngaythangnam.SelectionRange.Start.ToString("MM yyyy");  //dd MM yyyy
			ngay1 = ngaythangnam.SelectionRange.Start.ToString("dd");
			thang = ngaythangnam.SelectionRange.Start.ToString("MM");
			nam = ngaythangnam.SelectionRange.Start.ToString("yyyy");
			localClient.Publish("sub", Encoding.UTF8.GetBytes("getdata" + " " + ngay.Text));
			Int32.TryParse(ngay1, out ngayss);
			Int32.TryParse(thang, out  thangss);
			Int32.TryParse(nam, out  namss);
			start = 0;
			
			//MessageBox.Show(ngay1+" " + thang+" "+nam);
		}

		private void KillSpecificExcelFileProcess()
		{
			var processes = from p in Process.GetProcessesByName("EXCEL")
							select p;

			foreach (var process in processes)
			{
				try
				{
					if (process.MainWindowTitle == "KH-SX.xlsx - Excel" || process.MainWindowTitle == "Microsoft Excel - KH-SX" || process.MainWindowTitle == "Microsoft Excel" || process.MainWindowTitle == "KH-SX - Excel")
						process.Kill();
				}
				catch { }
			}
		}

		private void thoat_Click(object sender, EventArgs e)
		{
			GC.Collect();
			GC.WaitForPendingFinalizers();
			GC.Collect();
			GC.WaitForPendingFinalizers();
			KillSpecificExcelFileProcess();
			System.Windows.Forms.Application.Exit();
		}

		

		

		private void Client_MqttMsgPublishReceived(object sender, MqttMsgPublishEventArgs e)
		{
			
			message = Encoding.Default.GetString(e.Message);
			mestmp = message.Split(' ');
			//MessageBox.Show(message);

			try

			{
				
				//int load = 0;
				string ngay_dem = "";
					
					for (int i = 1; i < 32; i++)
					{
					//MessageBox.Show(message + " "+i.ToString());
						if (i < 10)
						{
							ngay_dem = "0" + i.ToString();
						}
						else { ngay_dem = i.ToString(); }
						if (mestmp[0].Equals("ngay" + ngay_dem))
						{
							if (repeat == 0)
							{
								repeat = 1;
								//MessageBox.Show("ĐANG NHẬN KẾT QUẢ, VUI LÒNG CHỜ !");
								if (pictureBox1.InvokeRequired && label2.InvokeRequired)
								{
									Invoke(new System.Action(() =>
									{
										pictureBox1.Visible = true;
										label2.Visible = true;
									}));
								}
								else { pictureBox1.Visible = true;
								label2.Visible = true;
								}
							
							}
							
							

							COMExcel.Application app = new COMExcel.Application();
							//MessageBox.Show("OK-222-----------------");
							COMExcel.Workbook workbook = app.Workbooks.Open("D:/Ke Hoach San Xuat/" + nam + "/KH-SX.xlsx");
							//MessageBox.Show(f + " " + j + " " + i);
							COMExcel.Worksheet xlWorksheet = (COMExcel.Worksheet)workbook.Sheets.get_Item(thangss);
							//COMExcel.Range xlRange = xlWorksheet.UsedRange;
							// Tạo mảng lưu trữ dữ liệu
							//object[,] valueArray = (object[,])xlRange.get_Value(COMExcel.XlRangeValueDataType.xlRangeValueDefault);

							workbook.Activate();
							xlWorksheet.Activate();
							app.Visible = false;
							app.DisplayAlerts = false;

							int p = 0;

							for (int l = 4; l < 20; l++)
							{
								//MessageBox.Show(l.ToString() + mestmp[p+3].ToString());
								xlWorksheet.Cells[l, i + i + 4] = mestmp[p += 3];
								xlWorksheet.Columns.AutoFit();

							}
							//app.Visible = true;

							workbook.Save();
							
							workbook.Close();
							app.Quit();
							
							System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook);
							System.Runtime.InteropServices.Marshal.ReleaseComObject(app);
							System.Runtime.InteropServices.Marshal.ReleaseComObject(xlWorksheet);
							GC.Collect();
							GC.WaitForPendingFinalizers();
							GC.Collect();
							GC.WaitForPendingFinalizers();
							KillSpecificExcelFileProcess();
							
						//break;
					}
					
				}
				if (mestmp[0].Equals("ngay31"))
				{

					//MessageBox.Show("ĐÃ THỰC HIỆN !");
					if (pictureBox1.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							pictureBox1.Visible = false;
							label2.Visible = false;
						}));
					}
					else
					{
						pictureBox1.Visible = false;
						label2.Visible = false;
					}
				}
				repeat = 0;


			}
				catch (Exception ex)
				{
					//MessageBox.Show("NOT SAVE_____________");
					//start = 0;
					KillSpecificExcelFileProcess();
				}
			
			}
		

		private void button1_Click(object sender, EventArgs e)
		{
			
			KillSpecificExcelFileProcess();
			GC.Collect();
			GC.WaitForPendingFinalizers();
			GC.Collect();
			GC.WaitForPendingFinalizers();
			Chuongtrinhchinh ctchinh = new Chuongtrinhchinh();    // Phai go dung ten Form tao truoc ****************

			ctchinh.Show();
			this.Close();
		}

		private void XUAT_DL_Click(object sender, EventArgs e)
		{
			
			try
			{
				if (namss != 0)
				{
					for (int i = 2019; i < 2030; i++)
					{
						for (int j = 1; j < 13; j++)
						{
							if (namss.Equals(i) && thangss.Equals(j))
							{
								//MessageBox.Show("OK-222-----------------");
								start = 0;
								
								COMExcel.Application app = new COMExcel.Application();
								COMExcel.Workbook workbook = app.Workbooks.Open("D:/Ke Hoach San Xuat/" + nam + "/KH-SX.xlsx");
								COMExcel.Worksheet xlWorksheet = (COMExcel.Worksheet)workbook.Sheets.get_Item(j);
								workbook.Activate();
								xlWorksheet.Activate();

								app.Visible = true;
								//app.Quit();
								app.DisplayAlerts = false;
								//System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook);
								//System.Runtime.InteropServices.Marshal.ReleaseComObject(app);
								//System.Runtime.InteropServices.Marshal.ReleaseComObject(xlWorksheet); 
							}

						}
					}
				}
				else { MessageBox.Show("Vui lòng chọn ngày !"); }
			}
			catch (Exception ex)
			{
				MessageBox.Show("Vui lòng cập nhật lại giờ máy tính!");
				KillSpecificExcelFileProcess();
				GC.Collect();
				GC.WaitForPendingFinalizers();
				GC.Collect();
				GC.WaitForPendingFinalizers();
			}
		}
	}
}
