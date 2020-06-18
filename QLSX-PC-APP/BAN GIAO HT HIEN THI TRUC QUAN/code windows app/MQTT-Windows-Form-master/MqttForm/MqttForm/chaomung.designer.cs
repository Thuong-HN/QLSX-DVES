namespace MqttForm
{
	partial class chaomung
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
			this.nhap = new System.Windows.Forms.TextBox();
			this.gui = new System.Windows.Forms.Button();
			this.dong = new System.Windows.Forms.Button();
			this.SuspendLayout();
			// 
			// nhap
			// 
			this.nhap.Font = new System.Drawing.Font("Times New Roman", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.nhap.Location = new System.Drawing.Point(12, 21);
			this.nhap.Multiline = true;
			this.nhap.Name = "nhap";
			this.nhap.Size = new System.Drawing.Size(353, 141);
			this.nhap.TabIndex = 0;
			this.nhap.TextChanged += new System.EventHandler(this.nhap_TextChanged);
			// 
			// gui
			// 
			this.gui.AutoSize = true;
			this.gui.BackColor = System.Drawing.Color.Brown;
			this.gui.Cursor = System.Windows.Forms.Cursors.Default;
			this.gui.Font = new System.Drawing.Font("UTM HelvetIns", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.gui.ForeColor = System.Drawing.Color.White;
			this.gui.Location = new System.Drawing.Point(43, 176);
			this.gui.Name = "gui";
			this.gui.Size = new System.Drawing.Size(88, 56);
			this.gui.TabIndex = 1;
			this.gui.Text = "GỬI";
			this.gui.UseVisualStyleBackColor = false;
			this.gui.Click += new System.EventHandler(this.gui_Click);
			// 
			// dong
			// 
			this.dong.AutoSize = true;
			this.dong.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(0)))));
			this.dong.Font = new System.Drawing.Font("UTM HelvetIns", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.dong.ForeColor = System.Drawing.Color.White;
			this.dong.Location = new System.Drawing.Point(239, 176);
			this.dong.Name = "dong";
			this.dong.Size = new System.Drawing.Size(86, 56);
			this.dong.TabIndex = 2;
			this.dong.Text = "ĐÓNG";
			this.dong.UseVisualStyleBackColor = false;
			this.dong.Click += new System.EventHandler(this.dong_Click);
			// 
			// chaomung
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
			this.ClientSize = new System.Drawing.Size(377, 244);
			this.Controls.Add(this.dong);
			this.Controls.Add(this.gui);
			this.Controls.Add(this.nhap);
			this.Name = "chaomung";
			this.Text = "Chào mừng";
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.TextBox nhap;
		private System.Windows.Forms.Button gui;
		private System.Windows.Forms.Button dong;
	}
}