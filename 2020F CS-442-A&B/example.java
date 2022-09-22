import java.sql.*;

/**
 * Max Shi
 * CS 442 SQL lab
 * I pledge my honor that I have abided by the Stevens Honor System.
 */
public class example {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost/test";

    //  Database credentials
    static final String USER = "root";
    //the user name; You can change it to your username (by default it is root).
    static final String PASS = "password";
    //the password; You can change it to your password (the one you used in MySQL server configuration).

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            //STEP 1: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 2: Open a connection to database
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            System.out.println("Creating database...");
            stmt = conn.createStatement();

            //STEP 3: Use SQL to Create Database;
            String sql = "CREATE DATABASE VehicleOffice";
            stmt.executeUpdate(sql);
            System.out.println("Database created successfully...");

            //STEP 4: Use SQL to select the database;
            sql = "use VehicleOffice";
            stmt.executeUpdate(sql);

            //STEP 5: Use SQL to create Tables;
            //STEP 5.1: Create Table Branch;
            sql = "create table branch( branch_id integer not null PRIMARY KEY, " +
                    "branch_name varchar(20) not null," +
                    "branch_addr varchar(50)," +
                    "branch_city varchar(20) not null," +
                    "branch_phone integer)";
            stmt.executeUpdate(sql);

            //STEP 5.2: Create Table Driver;
            sql = "create table driver(" +
                    "driver_ssn integer not null PRIMARY KEY," +
                    "driver_name varchar(20) not null," +
                    "driver_addr varchar(50) not null," +
                    "driver_city varchar(20) not null," +
                    "driver_birthdate date not null," +
                    "driver_phone integer)";
            stmt.executeUpdate(sql);

            //STEP 5.3: Create Table License;
            //Your Task 1!
            sql = "create table license(" +
                    "license_no integer not null PRIMARY KEY," +
                    "driver_ssn integer not null," +
                    "license_type char not null," +
                    "license_class integer not null," +
                    "license_expiry date not null," +
                    "issue_date date not null," +
                    "branch_id integer not null)";
            stmt.executeUpdate(sql);
            //STEP 5.4: Create Table Exam;
            //Your Task 2!
            sql = "create table exam(driver_ssn integer not null," +
                    "branch_id integer not null," +
                    "exam_date date not null," +
                    "exam_type char not null," +
                    "exam_score integer," +
                    "PRIMARY KEY (driver_ssn, branch_id, exam_date))";
            stmt.executeUpdate(sql);

            //STEP 6: Use SQL to insert tuples into tables;
            //STEP 6.1: insert tuples into Table Branch;
            sql = "insert into branch values(10, 'Main', '1234 Main St.', 'Hoboken', 5551234)";
            stmt.executeUpdate(sql);

            sql = "insert into branch values(20, 'NYC', '23 No.3 Road', 'NYC', 5552331)";
            stmt.executeUpdate(sql);

            //Your Task 3: insert the rest of tuples in Table Branch;
            sql = "insert into branch values(30, 'West Creek', '251 Creek Rd.', 'Newark', '5552511')";
            stmt.executeUpdate(sql);
            sql = "insert into branch values(40, 'Blenheim', '1342 W.22 Ave.', 'Princeton', '5551342')";
            stmt.executeUpdate(sql);

            //STEP 6.2: insert tuples into Table driver;
            sql = "insert into driver values(11111111, 'Bob Smith', '111 E. 11 St.', 'Hoboken', '1975-01-01', 5551111)";
            stmt.executeUpdate(sql);

            sql = "insert into driver values(22222222, 'John Walters', '222 E. 22 St.', 'Princeton', '1976-02-02', 5552222)";
            stmt.executeUpdate(sql);


            //Your Task 4: insert the rest of tuples in Table Driver;
            sql = "insert into driver values(33333333, 'Troy Rops', '333 W. 33 Ave', 'NYC', '1970-03-03', 5553333)";
            stmt.executeUpdate(sql);
            sql = "insert into driver values(44444444, 'Kevin Mark', '444 E. 4 Ave.', 'Hoboken', '1974-04-04', 5554444)";
            stmt.executeUpdate(sql);
            //STEP 6.3: insert tuples into Table license;
            //Your Task 5: insert all tuples into Table license;
            sql = "insert into license values(1, 11111111, 'D', 5, '2022-05-24', '2017-05-25', 20)";
            stmt.executeUpdate(sql);
            sql = "insert into license values(2, 22222222, 'D', 5, '2023-08-29', '2017-08-29', 40)";
            stmt.executeUpdate(sql);
            sql = "insert into license values(3, 33333333, 'L', 5, '2022-12-27', '2017-06-27', 20)";
            stmt.executeUpdate(sql);
            sql = "insert into license values(4, 44444444, 'D', 5, '2022-08-30', '2017-08-30', 40)";
            stmt.executeUpdate(sql);
            //STEP 6.4: insert all tuples into Table exam;
            //Your Task 6: insert all tuples into Table exam;
            sql = "insert into exam values(11111111, 20, '2017-05-25', 'D', 79)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(11111111, 20, '2017-12-02', 'L', 67)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(22222222, 30, '2016-05-06', 'L', 25)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(22222222, 40, '2016-06-10', 'L', 51)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(22222222, 40, '2016-08-29', 'D', 81)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(33333333, 10, '2017-07-07', 'L', 45)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(33333333, 20, '2017-06-27', 'L', 49)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(33333333, 20, '2017-07-27', 'L', 61)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(44444444, 10, '2017-07-27', 'L', 71)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(44444444, 20, '2017-08-30', 'L', 65)";
            stmt.executeUpdate(sql);
            sql = "insert into exam values(44444444, 40, '2017-09-01', 'L', 62)";
            stmt.executeUpdate(sql);
            //STEP 7: Use SQL to ask queries and retrieve data from the tables;
            //An example to retrieve branch ID, name, address from Table Branch, and display these values;
            Statement s = conn.createStatement();
            s.executeQuery("SELECT branch_id, branch_name, branch_addr FROM branch");
            ResultSet rs = s.getResultSet();
            int count = 0;
            while (rs.next()) {
                int idVal = rs.getInt("branch_id");
                String nameVal = rs.getString("branch_name");
                String addrVal = rs.getString("branch_addr");
                System.out.println(
                        "branch id = " + idVal
                                + ", name = " + nameVal
                                + ", address = " + addrVal);
                ++count;
            }
            rs.close();
            s.close();
            System.out.println(count + " rows were retrieved");

            //Your Task 7: Write SQL for Q1 - Q4 in Lab instruction and display the answers.
            //Q1
            s = conn.createStatement();
            s.executeQuery("SELECT driver_name FROM driver NATURAL JOIN license NATURAL JOIN branch WHERE branch_city='NYC'");
            rs = s.getResultSet();
            count = 0;
            while (rs.next()) {
                String nameVal = rs.getString("driver_name");
                System.out.println("name = " + nameVal);
                ++count;
            }
            rs.close();
            s.close();
            System.out.println(count + " rows were retrieved");

            //Q2
            s = conn.createStatement();
            s.executeQuery("SELECT driver_name FROM driver NATURAL JOIN license WHERE license_expiry<'2022-12-31'");
            rs = s.getResultSet();
            count = 0;
            while (rs.next()) {
                String nameVal = rs.getString("driver_name");
                System.out.println("name = " + nameVal);
                ++count;
            }
            rs.close();
            s.close();
            System.out.println(count + " rows were retrieved");

            s = conn.createStatement();
            s.executeQuery("SELECT driver_name FROM driver WHERE driver_ssn IN (SELECT driver_ssn FROM exam GROUP BY driver_ssn, branch_id, exam_type HAVING COUNT(*) >=2)");
            rs = s.getResultSet();
            count = 0;
            while (rs.next()) {
                String nameVal = rs.getString("driver_name");
                System.out.println("name = " + nameVal);
                ++count;
            }
            rs.close();
            s.close();
            System.out.println(count + " rows were retrieved");

            s = conn.createStatement();
            s.executeQuery("SELECT driver_name FROM driver WHERE driver_ssn NOT IN (SELECT E1.driver_ssn from exam E1, exam E2 where E1.exam_date < E2.exam_date AND E1.exam_score <= E2.exam_score AND E1.driver_ssn=E2.driver_ssn GROUP BY E1.driver_ssn)");
            rs = s.getResultSet();
            count = 0;
            while (rs.next()) {
                String nameVal = rs.getString("driver_name");
                System.out.println("name = " + nameVal);
                ++count;
            }
            rs.close();
            s.close();
            System.out.println(count + " rows were retrieved");

            //stmt.executeUpdate("DROP DATABASE vehicleoffice");
        } catch (SQLException se) {
            //Handle errors for JDBC
            se.printStackTrace();
        } catch (Exception e) {
            //Handle errors for Class.forName
            e.printStackTrace();
        } finally {
            //finally block used to close resources
            try {
                if (stmt != null)
                    stmt.close();
            } catch (SQLException se2) {
            }// nothing we can do
            try {
                if (conn != null)
                    conn.close();
            } catch (SQLException se) {
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}//end JDBCExample
