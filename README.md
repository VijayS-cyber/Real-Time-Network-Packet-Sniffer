# Real-Time-Network-Packet-Sniffer
This project develops a real-time network packet sniffer using Python. It captures live network packets, logs key header data into an SQLite database, detects anomalies like port scans and flooding, and displays live traffic summaries via a graphical interface with Matplotlib and Tkinter, enabling real-time network monitoring and alerts.

Procedure
1.Set Up Python Environment

Install Python 3.7 or higher.

Create and activate a virtual environment (recommended):

#text
python -m venv venv
source venv/bin/activate    # macOS/Linux  
.\venv\Scripts\Activate     # Windows PowerShell

2.Install Dependencies
Install the required Python packages:

#text
pip install scapy matplotlib

3.Initialize the Database
Run the script to create the SQLite database and tables:

#text
python init_db.py

4.Run the Packet Sniffer
Start real-time packet capturing and logging:

#text
python sniffer.py

Note: Run with administrator or root privileges to capture packets properly.

5.Launch the GUI Dashboard
In a separate terminal, start the live traffic visualization:

#text
python Live_traffic_gui.py
This displays a real-time protocol breakdown and traffic summary.

6.Monitor Alerts
The sniffer detects anomalies like port scans and flooding, printing alerts in the console and optionally logging or emailing them.

7.Stop the Sniffer
Terminate packet capture by pressing Ctrl+C in the terminal running sniffer.py.

Optional:

Configure email credentials in the sniffer to send real-time email alerts.

Customize thresholds and packet filters as needed in the sniffer.py script.

Check out the files attached to this repository.
