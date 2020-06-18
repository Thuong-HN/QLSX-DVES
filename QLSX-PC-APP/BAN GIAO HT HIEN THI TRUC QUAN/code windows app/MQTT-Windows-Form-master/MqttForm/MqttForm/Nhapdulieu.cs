using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;

namespace MqttForm
{
	public partial class Nhapdulieu : Form
	{
		
		private MqttClient localClient;
		public Nhapdulieu()
		{
			InitializeComponent();
			
		}

		private void Gui_dulieu_Click(object sender, EventArgs e)
		{
			if (txtNhap.Text != "")
			{
				try
				{
					//localClient.ProtocolVersion = MqttProtocolVersion.Version_3_1; // Giup ko bi loi connect khi mo task moi co
					localClient = new uPLibrary.Networking.M2Mqtt.MqttClient("10.11.15.70");
					string clientId = Guid.NewGuid().ToString();
					localClient.Connect(clientId);

					localClient.Subscribe(new String[] { "pub" }, new byte[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });

					//localClient.MqttMsgPublishReceived += Client_MqttMsgPublishReceived;
					localClient.Publish("sub", Encoding.UTF8.GetBytes(txtNhap.Text), uPLibrary.Networking.M2Mqtt.Messages.MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE, false);
				}
				catch (Exception ex)
				{
					Console.WriteLine("Connection Failed: " + ex.Message);
					MessageBox.Show("KHÔNG CÓ KẾT NỐI!");
				}
				
				//StreamWriter savedataKH2 = new StreamWriter("C:/Program Files (x86)/NMNHIP/THACO/Input/kehoach.txt");
				//savedataKH.WriteLine("KH2" + ' ' + txtdl9.Text + ' ');
				this.Hide();
				Chuongtrinhchinh Chuongtrinhchinh = new Chuongtrinhchinh();
				Chuongtrinhchinh.Show();
			}
		}

		private void button2_Click(object sender, EventArgs e)
		{
			this.Hide();
			Chuongtrinhchinh Chuongtrinhchinh = new Chuongtrinhchinh();
			Chuongtrinhchinh.Show();
		}
	}
}
