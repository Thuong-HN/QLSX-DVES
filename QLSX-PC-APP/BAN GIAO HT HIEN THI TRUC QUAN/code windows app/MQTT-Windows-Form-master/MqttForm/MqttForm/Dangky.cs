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

namespace MqttForm
{
    public partial class Dangky : Form
    {
        private static int counter=0,flag;
        public Dangky()
        {
            InitializeComponent();
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            Dangnhap DN = new Dangnhap();
            DN.Show();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string line;
            counter++;
      
                    MessageBox.Show("Đăng ký thành công !");

			 StreamWriter txt = new StreamWriter("C:/Program Files (x86)/NMNHIP/THACO/Input/demo.txt");
			//StreamWriter txt = new StreamWriter("/home/pi/thuong/demo.txt");
			//txt.WriteLine(counter);
			txt.WriteLine(txttk.Text);
                    txt.WriteLine(txtmk.Text);
                    txt.WriteLine(txtdc.Text);
                    txt.WriteLine(txtct.Text);
                    txt.WriteLine(txtcd.Text);
                    //txt.WriteLine("user");
                    //txt.WriteLineAsync();
                    txt.Close();                                      
                    
                }
            
               
            
            }
            
        
    
}
