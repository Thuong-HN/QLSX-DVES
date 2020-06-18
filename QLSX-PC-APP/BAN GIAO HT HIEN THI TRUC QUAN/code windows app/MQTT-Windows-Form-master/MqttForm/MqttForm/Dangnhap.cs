using System;

using System.IO;

using System.Windows.Forms;

namespace MqttForm
{
     
    public partial class Dangnhap : Form
    {
        //public static string taikhoan { get; private set; }
        //public static string matkhau { get; private set; }
        private int flag;
        public static int Remember { get; private set; }
		

		public Dangnhap()
        {
            InitializeComponent();
			 StreamReader txt1 = new StreamReader("C:/Program Files (x86)/NMNHIP/THACO/Input/check.txt");
			//StreamReader txt1 = new StreamReader("/home/pi/thuong/check.txt");
			string line,line2,line4; 
            int counter=0;
           // line = txt1.ReadLine();
            while ((line = txt1.ReadLine()) != null)
            {
                //MessageBox.Show("while");
                counter++;
                if ( line=="checked") {
					//MessageBox.Show("checked");                   
					//MessageBox.Show("checked2");
					StreamReader txt2 = new StreamReader("C:/Program Files (x86)/NMNHIP/THACO/Input/demo.txt");
					//StreamReader txt2 = new StreamReader("/home/pi/thuong/demo.txt");
					line2 = txt2.ReadLine();   // dòng 1
                        txtTK.Text = (line2);   
                        line4 = txt2.ReadLine();   // muon lay dong thu 2 thif khai bao bien khac doc dong ke tiep / dòng 2
                        txtMK.Text = (line4);
                        chkLuu.Checked = true;
                        txt2.Close();
                    
               
                }
                else chkLuu.Checked = false;
            }
            txt1.Close();
            

        }   
        private void btnDK_Click(object sender, EventArgs e)
        {

            
            Dangky  Dangky = new Dangky();    // Phai go dung ten Form tao truoc ****************
            //int milliseconds = 2000;
            //Task.Delay(milliseconds);
            
            Dangky.Show();
            this.Hide();
            //this.Close();
        }

        private void btnThoat_Click(object sender, EventArgs e)
        {
            
            MessageBox.Show("Bạn muốn đóng ứng dụng", "Đóng ứng dụng",MessageBoxButtons.YesNo);
			Application.Exit();
		}

        private void chkLuu_CheckedChanged(object sender, EventArgs e)
        {
            if (chkLuu.Checked == true)
            {
                flag = 1;
            }
            else flag = 0;
        }
        private void btnDN_Click(object sender, EventArgs e)
        {
            
            if (flag==1)
            {
                string check;
				StreamWriter txt = new StreamWriter("C:/Program Files (x86)/NMNHIP/THACO/Input/check.txt");
				//StreamWriter txt = new StreamWriter("/home/pi/thuong/check.txt");
				txt.WriteLine(check = "checked");
                //txt.WriteLine(txtTK.Text);
                //txt.WriteLine(txtMK.Text);              
                txt.Close();
            }
            else
            {
                string check;
				 StreamWriter txt = new StreamWriter("C:/Program Files (x86)/NMNHIP/THACO/Input/check.txt");
				//StreamWriter txt = new StreamWriter("/home/pi/thuong/check.txt");
				txt.WriteLine(check = "unchecked");
                //txt.WriteLine("");
                //txt.WriteLine("");               
                txt.Close();
            }
            string taikhoan = txtTK.Text;
            string matkhau = txtMK.Text;
            string line3,line5;
			StreamReader txt3 = new StreamReader("C:/Program Files (x86)/NMNHIP/THACO/Input/demo.txt");
			//StreamReader txt3 = new StreamReader("/home/pi/thuong/demo.txt");
			line3 = txt3.ReadLine();
            string taikhoan1 = (line3);   
            line5 = txt3.ReadLine();
            string matkhau1 = (line5);
            txt3.Close();
            if (taikhoan==taikhoan1 && matkhau==matkhau1)
            {
				//MessageBox.Show("Đăng nhập thành công !");
				

				this.Hide();
                Chuongtrinhchinh Chuongtrinhchinh = new Chuongtrinhchinh();
                Chuongtrinhchinh.Show();
            }
            else MessageBox.Show("Đăng nhập không thành công !");
            


        }

        

    }
}
