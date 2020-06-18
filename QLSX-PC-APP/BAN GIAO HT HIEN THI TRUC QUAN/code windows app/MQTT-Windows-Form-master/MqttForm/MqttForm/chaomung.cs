using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;

namespace MqttForm
{
	public partial class chaomung : Form
	{
		private MqttClient localClient;
		
		public chaomung()
		{
			InitializeComponent();
			try
			{
				
				localClient = new uPLibrary.Networking.M2Mqtt.MqttClient("10.11.15.201");
				string clientId = Guid.NewGuid().ToString();
				localClient.Connect(clientId);

				localClient.Subscribe(new String[] { "pub" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });

				//localClient.MqttMsgPublishReceived += Client_MqttMsgPublishReceived;

			}
			catch (Exception )
			{
				//Console.WriteLine("Connection Failed: " + ex.Message);
				MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
			}
		}

		private void gui_Click(object sender, EventArgs e)
		{
			StreamWriter txt = new StreamWriter("C:/Program Files (x86)/NMNHIP/THACO/Input/kehoach.txt");
			txt.WriteLine("1");
			txt.Close();
			localClient.Publish("sub", Encoding.UTF8.GetBytes("welcome"+"@"+"open"+"@"+nhap.Text));

			Chuongtrinhchinh quaylai = new Chuongtrinhchinh();    // Phai go dung ten Form tao truoc ****************
			quaylai.Show();
			this.Hide();
		}

		private void dong_Click(object sender, EventArgs e)
		{
			StreamWriter txt = new StreamWriter("C:/Program Files (x86)/NMNHIP/THACO/Input/kehoach.txt");
			txt.WriteLine("0");
			txt.Close();
			localClient.Publish("sub", Encoding.UTF8.GetBytes("welcome"+"@"+"close"));
			Chuongtrinhchinh quaylai = new Chuongtrinhchinh();    // Phai go dung ten Form tao truoc ****************
			quaylai.Show();
			this.Close();
		}

		

		private void nhap_TextChanged(object sender, EventArgs e)
		{

		}
	}
}
