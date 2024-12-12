# RealTImeStockMonitor

### **Step-by-Step Instructions to replicate on your end**

#### **1. Update the System**
   - **Why**: To ensure all packages and system tools are up-to-date.
   - **Command**:
     ```bash
     sudo apt update && sudo apt upgrade -y
     ```

#### **2. Install Java**
   - **Why**: Kafka requires Java to run.
   - **Command**:
     ```bash
     sudo apt install openjdk-11-jdk -y
     java -version
     ```

#### **3. Download and Extract Kafka**
   - **Why**: Kafka is the core message broker we’ll use.
   - **Commands**:
     ```bash
     wget https://downloads.apache.org/kafka/<VERSION>/kafka_<VERSION>.tgz
     tar -xzf kafka_<VERSION>.tgz
     ```

#### **4. Move Kafka to `/usr/local`**
   - **Why**: To organize the Kafka installation into a standard directory.
   - **Command**:
     ```bash
     sudo mv kafka_<VERSION> /usr/local/kafka
     ```

#### **5. Add Kafka to the PATH**
   - **Why**: To make Kafka commands available globally.
   - **Commands**:
     ```bash
     nano ~/.bashrc
     ```
     Add this line:
     ```bash
     export PATH=$PATH:/usr/local/kafka/bin
     ```
     Then, reload the configuration:
     ```bash
     source ~/.bashrc
     ```

#### **6. Test Kafka Installation**
   - **Why**: To confirm Kafka commands are accessible.
   - **Command**:
     ```bash
     kafka-topics.sh --version
     ```

#### **7. Install Python and Libraries**
   - **Why**: Python is used to write the producer and consumer scripts.
   - **Commands**:
     ```bash
     sudo apt install python3 python3-pip -y
     pip3 install kafka-python
     ```

#### **8. Set Up Project Folder**
   - **Why**: To organize our files for the project.
   - **Commands**:
     ```bash
     mkdir RealTimeStockMonitor
     cd RealTimeStockMonitor
     ```

#### **9. Create a Virtual Environment**
   - **Why**: To manage project-specific dependencies cleanly.
   - **Commands**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

#### **10. Install Python Dependencies**
   - **Why**: To install Kafka's Python library in the virtual environment.
   - **Command**:
     ```bash
     pip install kafka-python
     ```

#### **11. Start Zookeeper**
   - **Why**: Zookeeper is required for Kafka’s coordination.
   - **Command**:
     ```bash
     zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties
     ```

#### **12. Start Kafka**
   - **Why**: Kafka needs to run to handle message brokering.
   - **Command**:
     ```bash
     kafka-server-start.sh /usr/local/kafka/config/server.properties
     ```

#### **13. Create Kafka Topic**
   - **Why**: Topics are used for communication between producers and consumers.
   - **Commands**:
     ```bash
     kafka-topics.sh --create --topic stock_prices --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
     kafka-topics.sh --list --bootstrap-server localhost:9092
     ```

#### **14. Write Producer and Consumer Scripts**
   - **Why**: Producers generate stock prices, and consumers store them in the database.
   - **Command**:
     ```bash
     nano producer.py
     nano consumer.py
     ```

#### **15. Start the Producer**
   - **Why**: To begin sending stock price data to Kafka.
   - **Command**:
     ```bash
     python3 producer.py
     ```

#### **16. Start the Consumer**
   - **Why**: To consume the data from Kafka and store it in SQLite.
   - **Command**:
     ```bash
     python3 consumer.py
     ```

#### **17. Check Stored Data in SQLite**
   - **Why**: To verify that the data has been stored correctly.
   - **Commands**:
     ```bash
     sqlite3 stocks.db
     SELECT * FROM stock_prices;
     ```

---

### **Summary of What We Did**

1. Updated the system and installed necessary tools (Java and Python).
2. Downloaded, installed, and configured Kafka.
3. Created a Python project folder with a virtual environment and installed Kafka Python library.
4. Started Zookeeper and Kafka in separate terminals.
5. Created a Kafka topic and wrote producer/consumer scripts.
6. Ran producer and consumer scripts in separate terminals.
7. Queried the SQLite database to confirm successful data storage.
