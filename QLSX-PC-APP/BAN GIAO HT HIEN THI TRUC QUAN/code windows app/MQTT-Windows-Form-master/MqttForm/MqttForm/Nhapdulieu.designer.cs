namespace MqttForm
{
	partial class Nhapdulieu
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Nhapdulieu));
			this.NHAPNOIDUNG = new System.Windows.Forms.GroupBox();
			this.button2 = new System.Windows.Forms.Button();
			this.Gui_dulieu = new System.Windows.Forms.Button();
			this.txtNhap = new System.Windows.Forms.TextBox();
			this.NHAPNOIDUNG.SuspendLayout();
			this.SuspendLayout();
			// 
			// NHAPNOIDUNG
			// 
			this.NHAPNOIDUNG.BackColor = System.Drawing.SystemColors.ActiveCaption;
			this.NHAPNOIDUNG.Controls.Add(this.button2);
			this.NHAPNOIDUNG.Controls.Add(this.Gui_dulieu);
			this.NHAPNOIDUNG.Controls.Add(this.txtNhap);
			this.NHAPNOIDUNG.Font = new System.Drawing.Font("UTM HelvetIns", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.NHAPNOIDUNG.ForeColor = System.Drawing.Color.Magenta;
			this.NHAPNOIDUNG.Location = new System.Drawing.Point(60, 30);
			this.NHAPNOIDUNG.Name = "NHAPNOIDUNG";
			this.NHAPNOIDUNG.Size = new System.Drawing.Size(678, 408);
			this.NHAPNOIDUNG.TabIndex = 0;
			this.NHAPNOIDUNG.TabStop = false;
			this.NHAPNOIDUNG.Text = "NHẬP NỘI DUNG";
			// 
			// button2
			// 
			this.button2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(64)))), ((int)(((byte)(0)))));
			this.button2.ForeColor = System.Drawing.Color.Blue;
			this.button2.Location = new System.Drawing.Point(395, 315);
			this.button2.Name = "button2";
			this.button2.Size = new System.Drawing.Size(146, 70);
			this.button2.TabIndex = 2;
			this.button2.Text = "HỦY";
			this.button2.UseVisualStyleBackColor = false;
			this.button2.Click += new System.EventHandler(this.button2_Click);
			// 
			// Gui_dulieu
			// 
			this.Gui_dulieu.BackColor = System.Drawing.Color.Yellow;
			this.Gui_dulieu.ForeColor = System.Drawing.Color.Blue;
			this.Gui_dulieu.Location = new System.Drawing.Point(131, 315);
			this.Gui_dulieu.Name = "Gui_dulieu";
			this.Gui_dulieu.Size = new System.Drawing.Size(143, 70);
			this.Gui_dulieu.TabIndex = 1;
			this.Gui_dulieu.Text = "GỬI DỮ LIỆU";
			this.Gui_dulieu.UseVisualStyleBackColor = false;
			this.Gui_dulieu.Click += new System.EventHandler(this.Gui_dulieu_Click);
			// 
			// txtNhap
			// 
			this.txtNhap.Location = new System.Drawing.Point(34, 35);
			this.txtNhap.Multiline = true;
			this.txtNhap.Name = "txtNhap";
			this.txtNhap.Size = new System.Drawing.Size(618, 274);
			this.txtNhap.TabIndex = 0;
			// 
			// Nhapdulieu
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(800, 481);
			this.Controls.Add(this.NHAPNOIDUNG);
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Name = "Nhapdulieu";
			this.Text = "NHẬP NỘI DUNG HIỂN THỊ ";
			this.NHAPNOIDUNG.ResumeLayout(false);
			this.NHAPNOIDUNG.PerformLayout();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.GroupBox NHAPNOIDUNG;
		private System.Windows.Forms.Button button2;
		private System.Windows.Forms.Button Gui_dulieu;
		private System.Windows.Forms.TextBox txtNhap;
	}
}