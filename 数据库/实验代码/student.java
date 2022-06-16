/*
package dao;

import org.postgresql.copy.CopyManager;
import org.postgresql.core.BaseConnection;

import java.io.FileReader;
import java.io.IOException;
*/
import java.nio.charset.Charset;
import com.csvreader.CsvReader;
import java.sql.*;

public class student {
    static final String JDBC_DRIVER = "org.postgresql.Driver";  
    static final String DB_URL = "jdbc:postgresql://124.70.14.98:26000/demo?ApplicationName=app1";
      // 数据库的用户名与密码，需要根据自己的设置
    static final String USER = "dbuser";
    static final String PASS = "Gauss#3demo";
     public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pstmt=null;
        try{
            Class.forName(JDBC_DRIVER);
            System.out.println("正在连接数据库");
            conn = DriverManager.getConnection(DB_URL,USER,PASS);

            String sql="INSERT INTO mydb.new_s390(S#,SNAME,SEX,BDATE,HEIGHT,DORM) VALUES(?,?,?,?,?,?)";
            pstmt=(PreparedStatement) conn.prepareStatement(sql);
            CsvReader reader = new CsvReader("C:/Users/86199/Desktop/allstudent.csv",',',Charset.forName("GBK"));
            reader.readHeaders(); //跳过表头,不跳可以注释掉
            int i=0;
            while(reader.readRecord()){
                //此处顺序有误
                String[] str = reader.getValues();
                pstmt.setString(1,str[0]);
                pstmt.setString(2,str[1]);
                pstmt.setString(3,str[2]);
                pstmt.setString(4,str[3]);
                pstmt.setFloat(5,Float.parseFloat(str[4])); 
                pstmt.setString(6,str[5]);
                pstmt.addBatch();
                i=i+1;
                System.out.println(i);
                pstmt.executeBatch();
                }
        }catch(SQLException se){
            // 处理 JDBC 错误
            se.printStackTrace();
        }catch(Exception e){
            // 处理 Class.forName 错误
            e.printStackTrace();
        }finally{
            // 关闭资源
            try{
                if(pstmt!=null) pstmt.close();
            }catch(SQLException se2){
            }// 什么都不做
            try{
                if(conn!=null){
                    conn.close();
                }
            }catch(SQLException se){
                se.printStackTrace();
            }
        }
        System.out.println("INSERT SUCCESSFULLY!");
    }
}
