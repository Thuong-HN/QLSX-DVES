
using System;
using System.IO;
using System.Text;

using System.Windows.Forms;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using COMExcel = Microsoft.Office.Interop.Excel;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics;
using System.Threading;
using uPLibrary.Networking.M2Mqtt.Exceptions;
//using Microsoft.Office.Interop.Excel;

namespace MqttForm
{
	public partial class Chuongtrinhchinh : Form
    {
		
		private MqttClient localClient;
		string message = "";
		private string[] mestmp;
		
		private string dayss,monthss,yearss;
		private int tong1, tong2, tong3, tong4, tong5, tong6, tong7, tong8, tong9, tong10, tong11, tong12, tong13, tong14, tong15, tong16;
		Boolean a = false;
		private void timer1_Tick(object sender, EventArgs e)
		{
			a = !a;
			if (!a)
			{
				Nhap_lieu.BackColor = System.Drawing.Color.Red;
			}
			else { Nhap_lieu.BackColor = System.Drawing.Color.Lavender; }
			//MessageBox.Show("TIMER");
			
			//Thread.Sleep(500);
			//Nhap_lieu.BackColor = System.Drawing.Color.Yellow;
			
		}

		private int kh1, kh2, kh3, kh4, kh5, kh6, kh7, ngayss, kh9, kh10, kh11, kh12, kh13, kh14, khtong, khmonttong;
		private string ngay_1, ngay_2, ngay_3, ngay_4, ngay_5, ngay_6, ngay_7, ngay_8, ngay_9, ngay_10, ngay_11, ngay_12, ngay_13, ngay_14, ngay_15, ngay_16, ngay_17, ngay_18, ngay_19, ngay_20, ngay_21, ngay_22, ngay_23, ngay_24, ngay_25, ngay_26, ngay_27, ngay_28, ngay_29, ngay_30, ngay_31;
		private object xlWorksheet;
		private int namss, thangss,nam;
		private void txtdl9_TextChanged(object sender, EventArgs e)
		{

		}

		private void splitter1_SplitterMoved(object sender, SplitterEventArgs e)
		{

		}

		// ĐÓNG FILE EXCEL CÓ TÊN CỤ THỂ LẠI TRƯỚC KHI MỞ LẠI FILE
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
		
		

		private void NHAP_KEHOACH_Click(object sender, EventArgs e)
		{
			// ĐÓNG TOÀN BỘ FILE EXCEL
			/*System.Diagnostics.Process[] process = System.Diagnostics.Process.GetProcessesByName("Excel");
			foreach (System.Diagnostics.Process p in process)
			{
				if (!string.IsNullOrEmpty(p.ProcessName))
				{
					try
					{
						p.Kill();
					}
					catch { }
				}
			} */
			
			try
			{
				KillSpecificExcelFileProcess();


				// BẮT BUỘC PHẢI SAVE => THOÁT EXCEL TRƯỚC KHI UPDATE
				DateTime realtime = DateTime.Now;
				String ngay = (realtime.ToString("dd/MM/yyyy"));

				dayss = (realtime.ToString("dd"));
				monthss = (realtime.ToString("MM"));
				yearss = (realtime.ToString("yyyy"));
				Int32.TryParse(monthss, out  thangss);
				Int32.TryParse(yearss, out  namss);

				txtdlngay.Text = ngay;

				COMExcel.Application xllApp = new COMExcel.Application();
				//COMExcel.Workbook xllWorkbook = xllApp.Workbooks.Open("D:/Ke Hoach San Xuat/KH-SX-v15.xlsx");
				// Lấy Sheet 1
				for (int i = 2019; i < 2030; i++)
				{
					for (int j = 1; j < 13; j++)
					{
						if (namss.Equals(i) && thangss.Equals(j))
						{
							COMExcel.Workbook xllWorkbook = xllApp.Workbooks.Open("D:/Ke Hoach San Xuat/" + yearss + "/KH-SX.xlsx");
							COMExcel.Worksheet xlWorksheet = (COMExcel.Worksheet)xllWorkbook.Sheets.get_Item(j);
							xllWorkbook.Activate();
							xlWorksheet.Activate();
							xllApp.Visible = true;
						}
					}
				}
				

			}
			catch (DivideByZeroException)
			{
				MessageBox.Show("KHÔNG THỂ MỞ FILE/XEM LẠI GIỜ CỦA MÁY TÍNH!");
				KillSpecificExcelFileProcess();
			} 
			
				Form1 nhap = new Form1();
				nhap.Show();
			this.Close();


		}

		private void XUAT_DULIEU_Click(object sender, EventArgs e)
		{
			MessageBox.Show("XUẤT KẾ HOẠCH!");
			
		}
		
		private void txtdl13_TextChanged(object sender, EventArgs e)
		{

		}

		private void txtdl10_TextChanged(object sender, EventArgs e)
		{

		}
		string chekchao = "";
		public Chuongtrinhchinh()
        {
            InitializeComponent();
			
			StreamReader txt2 = new StreamReader("C:/Program Files (x86)/NMNHIP/THACO/Input/kehoach.txt");
			//StreamReader txt2 = new StreamReader("/home/pi/thuong/demo.txt");
			chekchao = txt2.ReadLine();   // dòng 1
			txt2.Close();
			if (chekchao == null) { timer1.Stop(); }
			else
			{
				if (chekchao.Equals("1"))
				{

					timer1.Start();
				}
				else
				{
					timer1.Stop();
				}
			}
			DateTime realtime = DateTime.Now;
			String ngaysend = (realtime.ToString("dd MM yyyy"));
			dayss = (realtime.ToString("dd"));
			monthss = (realtime.ToString("MM"));
			yearss = (realtime.ToString("yyyy"));
			Int32.TryParse(monthss, out thangss);
			Int32.TryParse(yearss, out namss);
			Int32.TryParse(dayss, out ngayss);

			
			try
			{

				localClient = new MqttClient("10.11.15.201");
				string clientId = Guid.NewGuid().ToString();
				localClient.Connect(clientId);
				//MessageBox.Show(localClient.IsConnected.ToString());
				//MessageBox.Show("TRY !");
				//localClient.ProtocolVersion = MqttProtocolVersion.Version_3_1;
				
				localClient.Subscribe(new String[] { "pub" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });

				localClient.MqttMsgPublishReceived += Client_MqttMsgPublishReceived;
				connected.Image = Properties.Resources.connected;
				

			}
			catch (MqttConnectionException ex)
			{
				connected.Image = Properties.Resources.disconnect;
				MessageBox.Show("KHÔNG CÓ KẾT NỐI, KIỂM TRA KẾT NỐI MẠNG !");
				KillSpecificExcelFileProcess();
			}
			
			
		}

		private void Chuongtrinhchinh_Load(object sender, EventArgs e)
		{

			KillSpecificExcelFileProcess();

			DateTime realtime = DateTime.Now;
			String ngay = (realtime.ToString("dd/MM/yyyy"));


			txtdlngay.Text = ngay;
			
			COMExcel.Application xllApp = new COMExcel.Application();
			try
			{
				for (int i = 2019; i < 2030; i++)
				{

					for (int j = 1; j < 13; j++)
					{

						if (namss.Equals(i) && thangss.Equals(j))
						{
							
							COMExcel.Workbook xllWorkbook = xllApp.Workbooks.Open("D:/Ke Hoach San Xuat/" + yearss + "/KH-SX.xlsx");
							COMExcel.Worksheet xlWorksheet = (COMExcel.Worksheet)xllWorkbook.Sheets.get_Item(j);
							xllWorkbook.Activate();
							xlWorksheet.Activate();
							COMExcel.Range xlRange = xlWorksheet.UsedRange;
							
							// Tạo mảng lưu trữ dữ liệu
							object[,] valueArray = (object[,])xlRange.get_Value(COMExcel.XlRangeValueDataType.xlRangeValueDefault);
							for (int l = 4; l < 21; l++)
							{
								for (int k = 5; k < 66; k += 2)
								{
									if (valueArray[l, k] == null)
									{

										valueArray[l, k] = 0;
									}
								}
							}

							//MessageBox.Show("UPDATE THỰC HIỆN!");
							for (int t = 5; t < 64; t += 2)
							{

								// SO SÁNH NGÀY TRONG FILE VỚI NGÀY THỰC TẾ -> trùng thì update giá trị lên phần mềm
								DateTime savetime = DateTime.Now;
								String day = (savetime.Day.ToString("d"));   // LẤY NGÀY HIỆN TẠI

								if (day.Equals(valueArray[2, t].ToString()))
								{
									try
									{
										txtdl8.Text = valueArray[4, t].ToString();// txtdl1.Text = valueArray[4, t+1].ToString();   //THỰC HIỆN
										txtdl9.Text = valueArray[5, t].ToString();// txtdl2.Text = valueArray[5, t + 1].ToString();
										txtdl10.Text = valueArray[6, t].ToString();// txtdl3.Text = valueArray[6, t + 1].ToString();
										txtdl11.Text = valueArray[7, t].ToString(); //txtdl4.Text = valueArray[7, t + 1].ToString();
										txtdl12.Text = valueArray[8, t].ToString(); //txtdl5.Text = valueArray[8, t + 1].ToString();
										txtdl13.Text = valueArray[9, t].ToString(); //txtdl6.Text = valueArray[9, t + 1].ToString();
										txtdl14.Text = valueArray[10, t].ToString(); //txtdl7.Text = valueArray[10, t + 1].ToString();
										txtdl30.Text = valueArray[11, t].ToString();// txtdl29.Text = valueArray[11, t + 1].ToString();
										txtdl34.Text = valueArray[12, t].ToString();// txtdl33.Text = valueArray[12, t + 1].ToString();
										txtdl38.Text = valueArray[13, t].ToString();// txtdl37.Text = valueArray[13, t + 1].ToString();
										txtdl42.Text = valueArray[14, t].ToString();// txtdl41.Text = valueArray[14, t + 1].ToString();
										txtdl46.Text = valueArray[15, t].ToString();// txtdl45.Text = valueArray[15, t + 1].ToString();
										txtdl50.Text = valueArray[16, t].ToString();// txtdl49.Text = valueArray[16, t + 1].ToString();
										txtdl54.Text = valueArray[17, t].ToString();// txtdl53.Text = valueArray[17, t + 1].ToString();
										txtdl58.Text = valueArray[18, t].ToString();// txtdl57.Text = valueArray[18, t + 1].ToString();
										txtdl62.Text = valueArray[19, t].ToString();// txtdl61.Text = valueArray[19, t + 1].ToString();
										txtdlt2.Text = valueArray[20, t].ToString();// txtdlt1.Text = valueArray[20, t + 1].ToString();

									}
									catch (Exception ex)
									{

										//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
									}

									
								}
							}


							// CẬP NHẬT TÊN SẢN PHẨM
							sp_1.Text = valueArray[4, 1].ToString(); sp_2.Text = valueArray[6, 1].ToString(); sp_3.Text = valueArray[7, 1].ToString();
							sp_4.Text = valueArray[9, 1].ToString(); sp_5.Text = valueArray[11, 1].ToString(); sp_6.Text = valueArray[13, 1].ToString();
							sp_7.Text = valueArray[14, 1].ToString(); sp_8.Text = valueArray[15, 1].ToString(); sp_9.Text = valueArray[17, 1].ToString();
							sp_10.Text = valueArray[18, 1].ToString();


							// TỔNG THỰC HIỆN / THÁNG
							txtdl15.Text = valueArray[4, 68].ToString(); txtdl16.Text = valueArray[5, 68].ToString(); txtdl17.Text = valueArray[6, 68].ToString();
							txtdl18.Text = valueArray[7, 68].ToString(); txtdl19.Text = valueArray[8, 68].ToString(); txtdl20.Text = valueArray[9, 68].ToString();
							txtdl21.Text = valueArray[10, 68].ToString(); txtdl31.Text = valueArray[11, 68].ToString(); txtdl35.Text = valueArray[12, 68].ToString();
							txtdl39.Text = valueArray[13, 68].ToString(); txtdl43.Text = valueArray[14, 68].ToString(); txtdl47.Text = valueArray[15, 68].ToString();
							txtdl51.Text = valueArray[16, 68].ToString(); txtdl55.Text = valueArray[17, 68].ToString(); txtdl59.Text = valueArray[18, 68].ToString();
							txtdl63.Text = valueArray[19, 68].ToString(); txtdlt3.Text = valueArray[20, 68].ToString();

							//TỔNG KẾ HOẠCH / THÁNG
							txtdl22.Text = valueArray[4, 67].ToString(); txtdl23.Text = valueArray[5, 67].ToString(); txtdl24.Text = valueArray[6, 67].ToString();
							txtdl25.Text = valueArray[7, 67].ToString(); txtdl26.Text = valueArray[8, 67].ToString(); txtdl27.Text = valueArray[9, 67].ToString();
							txtdl28.Text = valueArray[10, 67].ToString(); txtdl32.Text = valueArray[11, 67].ToString(); txtdl36.Text = valueArray[12, 67].ToString();
							txtdl40.Text = valueArray[13, 67].ToString(); txtdl44.Text = valueArray[14, 67].ToString(); txtdl48.Text = valueArray[15, 67].ToString();
							txtdl52.Text = valueArray[16, 67].ToString(); txtdl56.Text = valueArray[17, 67].ToString(); txtdl60.Text = valueArray[18, 67].ToString();
							txtdl64.Text = valueArray[19, 67].ToString(); txtdlt4.Text = valueArray[20, 67].ToString();

							// SO SÁNH SỐ LƯỢNG THỰC HIỆN / THÁNG
							txttool1.Text = txtdlt3.Text;
							txtdlthang.Text = txtdlt4.Text;
							//THOÁT HOÀN TOÀN EXCEL
							xllWorkbook.Close();
							xllApp.Quit();
							System.Runtime.InteropServices.Marshal.ReleaseComObject(xllWorkbook);
							System.Runtime.InteropServices.Marshal.ReleaseComObject(xllApp);
							System.Runtime.InteropServices.Marshal.ReleaseComObject(xlWorksheet);
							KillSpecificExcelFileProcess();
							GC.Collect();
							GC.WaitForPendingFinalizers();
							GC.Collect();
							GC.WaitForPendingFinalizers();
						}
					}
				}

			}
			catch (Exception ex)
			{
				MessageBox.Show("KHÔNG THỂ MỞ FILE/XEM LẠI GIỜ CỦA MÁY TÍNH!");
				KillSpecificExcelFileProcess();
			}


		}
		private void Nhap_lieu_Click(object sender, EventArgs e)      // NHẬP CHÀO MỪNG
		{
			
			chaomung Nhapdulieu = new chaomung();    // Phai go dung ten Form tao truoc ****************
			Nhapdulieu.Show();
			this.Hide();
		}
		private void Client_MqttMsgPublishReceived(object sender, MqttMsgPublishEventArgs e)
		{
			
			message = Encoding.Default.GetString(e.Message);			
			mestmp = message.Split(' ');
			foreach (string word in mestmp)
			{
				//Console.WriteLine("WORD: " + word);
			}
			
			
			try
			{
				/*if (mestmp[0].Equals("getdata"))
				{
					
					// Lấy Sheet 1
					//COMExcel.Worksheet worksheet = (COMExcel.Worksheet)workbook.Sheets.get_Item(1);

					try
					{
						for (int i = 2019; i < 2030; i++)
						{
							for (int j = 1; j < 13; j++)
							{
								for (int f = 1; f < 32; f++)
								{
									if (namss.Equals(i) && thangss.Equals(j) && ngayss.Equals(f))
									{
										COMExcel.Application app = new COMExcel.Application();
										COMExcel.Workbook workbook = app.Workbooks.Open("D:/Ke Hoach San Xuat/" + yearss + "/KH-SX.xlsx");
										COMExcel.Worksheet xlWorksheet = (COMExcel.Worksheet)workbook.Sheets.get_Item(j);
										workbook.Activate();
										xlWorksheet.Activate();
										//COMExcel.Range xlRange = xlWorksheet.UsedRange;
										// Tạo mảng lưu trữ dữ liệu
										//object[,] valueArray = (object[,])xlRange.get_Value(COMExcel.XlRangeValueDataType.xlRangeValueDefault);
										//MessageBox.Show("OK-222-----------------");

										//MessageBox.Show("NHẬN GETDATA!");

										int p = 0;

										for (int l = 4; l < 20; l++)
										{
											//MessageBox.Show(l.ToString() + mestmp[p+3].ToString());
											xlWorksheet.Cells[l, f + f + 4] = mestmp[p += 3];
											app.Visible = false;
											
											app.DisplayAlerts = false;
											//worksheet.Columns.AutoFit();



										}
										workbook.Save();
										workbook.Close();
										app.Quit();
										System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook);
										System.Runtime.InteropServices.Marshal.ReleaseComObject(app);
										System.Runtime.InteropServices.Marshal.ReleaseComObject(xlWorksheet);
										KillSpecificExcelFileProcess();



									}
								}
							}
						}
						//KillSpecificExcelFileProcess();

					}
					catch (Exception ex)
					{
						KillSpecificExcelFileProcess();
					}





				} */
				if (mestmp[0].Equals("K250FT"))
				{   // nhíp sau
					if (txtdl1.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl1.Text = mestmp[1];
						}));
					}
					else { txtdl1.Text = mestmp[1]; }
					
					//StreamWriter sw = new StreamWriter("D:/Ke Hoach San Xuat/2019/thang-3/ngay-1.txt");
					//sw.WriteLine("K250FT" + " " + mestmp[1]);
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[4, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("K250RR"))
				{
					if (txtdl2.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl2.Text = mestmp[1];
						}));
					}
					else { txtdl2.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[5, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("K200"))
				{
					if (txtdl3.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl3.Text = mestmp[1];
						}));
					}
					else { txtdl3.Text = mestmp[1]; }
				/*	try
						{
						for (int j = 1; j < 32; j ++)
						{
							if (ngayss == j)
							{
								
									worksheet.Cells[6, j+j+4] = txtdl3.Text;
								
							}
						}
						
					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					}  */
				}
				if (mestmp[0].Equals("OLLIN500FT"))
				{
					if (txtdl4.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl4.Text = mestmp[1];
						}));
					}
					else { txtdl4.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[7, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("OLLIN500RR"))
				{
					if (txtdl5.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl5.Text = mestmp[1];
						}));
					}
					else { txtdl5.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[8, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("OLLIN500M3FT"))
				{
					if (txtdl6.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl6.Text = mestmp[1];
						}));
					}
					else { txtdl6.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[9, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("OLLIN500M3RR"))
				{
					if (txtdl7.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl7.Text = mestmp[1];
						}));
					}
					else { txtdl7.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[10, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("OLLIN700FT"))
				{
					if (txtdl29.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl29.Text = mestmp[1];
						}));
					}
					else { txtdl29.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[11, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("OLLIN700RR"))
				{
					if (txtdl33.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl33.Text = mestmp[1];
						}));
					}
					else { txtdl33.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[12, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("SMRM4LA"))
				{
					if (txtdl37.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl37.Text = mestmp[1];
						}));
					}
					else { txtdl37.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[13, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}         
				if (mestmp[0].Equals("SMRM7LA"))
				{
					if (txtdl41.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl41.Text = mestmp[1];
						}));
					}
					else { txtdl41.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[14, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("OLLIN700720FT"))
				{
					if (txtdl45.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl45.Text = mestmp[1];
						}));
					}
					else { txtdl45.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[15, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}  
				if (mestmp[0].Equals("OLLIN700720RR"))
				{
					if (txtdl49.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl49.Text = mestmp[1];
						}));
					}
					else { txtdl49.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[16, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("K190"))
				{
					if (txtdl53.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl53.Text = mestmp[1];
						}));
					}
					else { txtdl53.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[17, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				}
				if (mestmp[0].Equals("K165FT"))
				{
					if (txtdl57.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl57.Text = mestmp[1];
						}));
					}
					else { txtdl57.Text = mestmp[1]; }
				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[18, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */
				} 
				if (mestmp[0].Equals("K165RR"))
				{
					if (txtdl61.InvokeRequired)
					{
						Invoke(new System.Action(() =>
						{
							txtdl61.Text = mestmp[1];
						}));
					}
					else { txtdl61.Text = mestmp[1]; }

				/*	try
					{
						for (int j = 1; j < 32; j++)
						{
							if (ngayss == j)
							{

								worksheet.Cells[19, j + j + 4] = txtdl3.Text;

							}
						}

					}
					catch (Exception ex)
					{
						//Console.WriteLine("Connection Failed: " + ex.Message);
						//MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
					} */

				} 

				

					// CẢNH BÁO KHI SẢN XUẤT VƯỢT MỨC
				if (mestmp[0].Equals("WarnningK250FT"))
				{   // nhíp trước

					txtdl1.ForeColor = System.Drawing.Color.Red;

				}

				if (mestmp[0].Equals("WarnningK250RR"))
				{

					txtdl2.ForeColor = System.Drawing.Color.Red;

				}

				if (mestmp[0].Equals("WarnningK200"))
				{
					txtdl3.ForeColor = System.Drawing.Color.Red;
				}

				if (mestmp[0].Equals("WarnningOLLIN500FT"))
				{
					txtdl4.ForeColor = System.Drawing.Color.Red;
				}

				if (mestmp[0].Equals("WarnningOLLIN500RR"))
				{
					txtdl5.ForeColor = System.Drawing.Color.Red;
				}

				if (mestmp[0].Equals("WarnningOLLIN500M3FT"))
				{
					txtdl6.ForeColor = System.Drawing.Color.Red;

				}

				if (mestmp[0].Equals("WarnningOLLIN500M3RR"))
				{
					txtdl7.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningOLLIN700FT"))
				{
					txtdl29.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningOLLIN700RR"))
				{
					txtdl33.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningSMRM4LA"))
				{
					txtdl37.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningSMRM7LA"))
				{
					txtdl41.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningOLLIN700720FT"))
				{
					txtdl45.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningOLLIN700720RR"))
				{
					txtdl49.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningK190"))
				{
					txtdl53.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningK165FT"))
				{
					txtdl57.ForeColor = System.Drawing.Color.Red;
				}
				if (mestmp[0].Equals("WarnningK165RR"))
				{
					txtdl61.ForeColor = System.Drawing.Color.Red;
				}

				Int32.TryParse(txtdl1.Text, out tong1); Int32.TryParse(txtdl2.Text, out tong2); Int32.TryParse(txtdl3.Text, out tong3);
				Int32.TryParse(txtdl4.Text, out tong4); Int32.TryParse(txtdl5.Text, out tong5); Int32.TryParse(txtdl6.Text, out tong6);
				Int32.TryParse(txtdl7.Text, out tong7); Int32.TryParse(txtdl29.Text, out tong8); Int32.TryParse(txtdl33.Text, out tong9);
				Int32.TryParse(txtdl37.Text, out tong10); Int32.TryParse(txtdl41.Text, out tong11); Int32.TryParse(txtdl45.Text, out tong12);
				Int32.TryParse(txtdl49.Text, out tong13); Int32.TryParse(txtdl53.Text, out tong14); Int32.TryParse(txtdl57.Text, out tong15);
				Int32.TryParse(txtdl61.Text, out tong16);
				if (txtdl1.Text == "")
				{
					tong1 = 0;
				}
				if (txtdl2.Text == "")
				{
					tong2 = 0;
				}
				if (txtdl3.Text == "")
				{
					tong3 = 0;
				}
				if (txtdl4.Text == "")
				{
					tong4 = 0;
				}
				if (txtdl5.Text == "")
				{
					tong5 = 0;
				}
				if (txtdl6.Text == "")
				{
					tong6 = 0;
				}
				if (txtdl7.Text == "")
				{
					tong7 = 0;
				}
				if (txtdl29.Text == "")
				{
					tong8 = 0;
				}
				if (txtdl33.Text == "")
				{
					tong9 = 0;
				}
				if (txtdl37.Text == "")
				{
					tong10 = 0;
				}
				if (txtdl41.Text == "")
				{
					tong11 = 0;
				}
				if (txtdl45.Text == "")
				{
					tong12 = 0;
				}
				if (txtdl49.Text == "")
				{
					tong13 = 0;
				}
				if (txtdl53.Text == "")
				{
					tong14 = 0;
				}
				if (txtdl57.Text == "")
				{
					tong15 = 0;
				}
				if (txtdl61.Text == "")
				{
					tong16 = 0;
				}
				if (txtdlt1.InvokeRequired)
				{
					Invoke(new System.Action(() =>
					{
						txtdlt1.Text = (tong1 + tong2 + tong3 + tong4 + tong5 + tong6 + tong7 + tong8 + tong9 + tong10 + tong11 + tong12 + tong13 + tong14).ToString();
					}));
				}
				else { txtdlt1.Text = (tong1 + tong2 + tong3 + tong4 + tong5 + tong6 + tong7 + tong8 + tong9 + tong10 + tong11 + tong12 + tong13 + tong14).ToString(); }
/*
				if (mestmp[0].Equals("K250FT") || mestmp[0].Equals("K250RR") || mestmp[0].Equals("K200") || mestmp[0].Equals("OLLIN500FT") || mestmp[0].Equals("OLLIN500RR")
					|| mestmp[0].Equals("OLLIN500M3FT") || mestmp[0].Equals("OLLIN500M3RR") || mestmp[0].Equals("OLLIN700FT") || mestmp[0].Equals("OLLIN700RR")
					|| mestmp[0].Equals("SMRM4LA") || mestmp[0].Equals("SMRM7LA") || mestmp[0].Equals("OLLIN700720FT") || mestmp[0].Equals("OLLIN700720RR")
					|| mestmp[0].Equals("K190") || mestmp[0].Equals("K165FT") || mestmp[0].Equals("K165RR"))
				{
					txtdl15.Text = valueArray[4, 68].ToString(); txtdl16.Text = valueArray[5, 68].ToString(); txtdl17.Text = valueArray[6, 68].ToString();
					txtdl18.Text = valueArray[7, 68].ToString(); txtdl19.Text = valueArray[8, 68].ToString(); txtdl20.Text = valueArray[9, 68].ToString();
					txtdl21.Text = valueArray[10, 68].ToString(); txtdl31.Text = valueArray[11, 68].ToString(); txtdl35.Text = valueArray[12, 68].ToString();
					txtdl39.Text = valueArray[13, 68].ToString(); txtdl43.Text = valueArray[14, 68].ToString(); txtdl47.Text = valueArray[15, 68].ToString();
					txtdl51.Text = valueArray[16, 68].ToString(); txtdl55.Text = valueArray[17, 68].ToString(); txtdl59.Text = valueArray[18, 68].ToString();
					txtdl63.Text = valueArray[19, 68].ToString(); txtdlt3.Text = valueArray[20, 68].ToString();
				}  */   // Lấy giá trị thực hiện tháng hiển thị lên app real time

			/*	app.DisplayAlerts = false;
				//worksheet.Columns.AutoFit();
				workbook.Save();
				//workbook.Saved = true;
				//workbook.SaveAs(@"D:/Ke Hoach San Xuat/KH-SX-v15.xlsx", Microsoft.Office.Interop.Excel.XlFileFormat.xlOpenXMLWorkbook);

				workbook.Close(true);
				app.Quit();
				System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook);
				System.Runtime.InteropServices.Marshal.ReleaseComObject(app);
				System.Runtime.InteropServices.Marshal.ReleaseComObject(worksheet);
				KillSpecificExcelFileProcess(); 
				*/
			}
			catch (Exception ex)
			{
				//Console.WriteLine("Connection Failed: " + ex.Message);
				MessageBox.Show("LỖI KẾT NỐI !");
				KillSpecificExcelFileProcess();
			}
			
			
		}




		// *********

		private void Chuongtrinhchinh_Closing(object sender, FormClosingEventArgs e)
        {
			try
			{
				localClient.Disconnect();
				KillSpecificExcelFileProcess();
			}
			catch (Exception ex)
			{
				//Console.WriteLine("Connection Failed: " + ex.Message);
				//MessageBox.Show("ERROR");
			}

		}
        // *********


			
		private void btnthoat_Click(object sender, EventArgs e) 
		{

			try
			{
				localClient.Disconnect();
				KillSpecificExcelFileProcess();
			}
			catch (Exception ex)
			{
				KillSpecificExcelFileProcess();
				//Console.WriteLine("Connection Failed: " + ex.Message)
				//MessageBox.Show("ERROR");
			}

			Application.Exit();    // đóng hoàn toàn ứng dụng
			
			
			//this.Hide();
			//Dangnhap DN = new Dangnhap();
			//DN.Show();
		}

		private void btndata_Click(object sender, EventArgs e)
		{
			xuatdulieu xuatdulieu = new xuatdulieu();    // Phai go dung ten Form tao truoc ****************

			xuatdulieu.Show();
			this.Close();

		}              // GỬI KẾ HOẠCH ĐẾN MÀN HÌNH HIỂN THỊ

		

		
	}
	

         
}
