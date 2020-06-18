namespace MqttForm
{
	partial class xuatdulieu
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
			this.ngaythangnam = new System.Windows.Forms.MonthCalendar();
			this.label1 = new System.Windows.Forms.Label();
			this.ngay = new System.Windows.Forms.Label();
			this.button1 = new System.Windows.Forms.Button();
			this.XUAT_DL = new System.Windows.Forms.Button();
			this.thoat = new System.Windows.Forms.Button();
			this.label2 = new System.Windows.Forms.Label();
			this.pictureBox1 = new System.Windows.Forms.PictureBox();
			((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
			this.SuspendLayout();
			// 
			// ngaythangnam
			// 
			this.ngaythangnam.BackColor = System.Drawing.SystemColors.MenuHighlight;
			this.ngaythangnam.CalendarDimensions = new System.Drawing.Size(2, 1);
			this.ngaythangnam.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.ngaythangnam.Location = new System.Drawing.Point(7, 9);
			this.ngaythangnam.MaxSelectionCount = 2;
			this.ngaythangnam.Name = "ngaythangnam";
			this.ngaythangnam.SelectionRange = new System.Windows.Forms.SelectionRange(new System.DateTime(2019, 3, 23, 0, 0, 0, 0), new System.DateTime(2019, 3, 24, 0, 0, 0, 0));
			this.ngaythangnam.TabIndex = 0;
			this.ngaythangnam.TitleBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
			this.ngaythangnam.DateChanged += new System.Windows.Forms.DateRangeEventHandler(this.ngaythangnam_DateChanged);
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.BackColor = System.Drawing.Color.Transparent;
			this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
			this.label1.Location = new System.Drawing.Point(7, 198);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(73, 20);
			this.label1.TabIndex = 1;
			this.label1.Text = "THÁNG :";
			// 
			// ngay
			// 
			this.ngay.AutoSize = true;
			this.ngay.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.ngay.Location = new System.Drawing.Point(80, 194);
			this.ngay.Name = "ngay";
			this.ngay.Size = new System.Drawing.Size(0, 24);
			this.ngay.TabIndex = 2;
			// 
			// button1
			// 
			this.button1.BackColor = System.Drawing.Color.Lavender;
			this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.button1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(64)))), ((int)(((byte)(0)))));
			this.button1.Location = new System.Drawing.Point(297, 186);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(90, 41);
			this.button1.TabIndex = 3;
			this.button1.Text = "Quay Lại";
			this.button1.UseVisualStyleBackColor = false;
			this.button1.Click += new System.EventHandler(this.button1_Click);
			// 
			// XUAT_DL
			// 
			this.XUAT_DL.BackColor = System.Drawing.Color.WhiteSmoke;
			this.XUAT_DL.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.XUAT_DL.ForeColor = System.Drawing.Color.Blue;
			this.XUAT_DL.Location = new System.Drawing.Point(180, 186);
			this.XUAT_DL.Name = "XUAT_DL";
			this.XUAT_DL.Size = new System.Drawing.Size(111, 41);
			this.XUAT_DL.TabIndex = 4;
			this.XUAT_DL.Text = "XUẤT DỮ LIỆU";
			this.XUAT_DL.UseVisualStyleBackColor = false;
			this.XUAT_DL.Click += new System.EventHandler(this.XUAT_DL_Click);
			// 
			// thoat
			// 
			this.thoat.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.thoat.Location = new System.Drawing.Point(392, 186);
			this.thoat.Name = "thoat";
			this.thoat.Size = new System.Drawing.Size(75, 41);
			this.thoat.TabIndex = 5;
			this.thoat.Text = "Thoát";
			this.thoat.UseVisualStyleBackColor = true;
			this.thoat.Click += new System.EventHandler(this.thoat_Click);
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label2.ForeColor = System.Drawing.Color.Blue;
			this.label2.Location = new System.Drawing.Point(92, 221);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(299, 24);
			this.label2.TabIndex = 7;
			this.label2.Text = "Đang lấy kết quả, vui lòng đợi !";
			// 
			// pictureBox1
			// 
			this.pictureBox1.BackColor = System.Drawing.Color.Transparent;
			this.pictureBox1.Image = global::MqttForm.Properties.Resources.loader;
			this.pictureBox1.Location = new System.Drawing.Point(7, 9);
			this.pictureBox1.Name = "pictureBox1";
			this.pictureBox1.Size = new System.Drawing.Size(460, 268);
			this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
			this.pictureBox1.TabIndex = 6;
			this.pictureBox1.TabStop = false;
			// 
			// xuatdulieu
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(472, 289);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.pictureBox1);
			this.Controls.Add(this.thoat);
			this.Controls.Add(this.XUAT_DL);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.ngay);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.ngaythangnam);
			this.Name = "xuatdulieu";
			this.Text = "CHỌN NGÀY XUẤT DỮ LIỆU";
			((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.MonthCalendar ngaythangnam;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.Label ngay;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.Button XUAT_DL;
		private System.Windows.Forms.Button thoat;
		private System.Windows.Forms.PictureBox pictureBox1;
		private System.Windows.Forms.Label label2;
	}
}