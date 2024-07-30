package com.text.app;

import android.app.*;
import android.os.*;
import java.io.File;
import java.io.*;
import android.os.Build;
import android.content.Intent; 
import android.net.Uri;
import android.provider.Settings; 
import android.content.ActivityNotFoundException;
import android.app.Activity; 
import android.content.Context;
import android.os.Environment;
import android.util.*;
import android.widget.*;
import java.util.*;

public class filehelp
{
private Context context;
public filehelp(Context context){
	this.context=context;
}
//申请权限
public void getpermission(Activity activity){
	if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) { 
		if (Environment.isExternalStorageManager()) {} else { 
		Intent intent = new Intent(Settings.ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION); 
		Uri uri = Uri.fromParts("package", context.getPackageName(), null); 
		intent.setData(uri); 
		activity.startActivityForResult(intent, 1); 
			} 
		}
	}
//在sd卡根目录中创建文件夹
public File buildfolder(String foldername){
	File customDir = new File(Environment.getExternalStorageDirectory(), foldername);//Environment.getExternalStorageDirectory()获取根目录
	if (Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState())) {
		if (!customDir.exists()) {customDir.mkdirs();}
		}
	return customDir;
}
public File buildfile(File foldername,String filename){
	File file = new File(foldername,filename);
			
	if (Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState())) {
	 	try{
			file.createNewFile();
			}catch(IOException e){}
	}
	return file;
}
//向某个文件中写入字符串
public void writecontent(File file,String content){
	if (Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState())) {
	 	try{
			FileOutputStream fos = new FileOutputStream(file, false);
			fos.write(content.getBytes());
			fos.close();
			}catch(IOException e){}
	}
}
//删除某个文件夹
public void deletefolder(File directory) {
    if (directory.exists() && Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState())) {
        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    deletefolder(file); // 递归删除子目录
                } else {
                    file.delete(); // 删除文件
                }
            }
        }
        directory.delete(); // 删除空目录
    }
}
//删除某个文件
public void deletefile(File file) {
    if (file.exists() && Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState())) {
        file.delete();
    	}
	}
//读取某个文件中的字符串
public String readfile(File file) {
    try {
        FileInputStream input = new FileInputStream(file);
        byte[] temp = new byte[1024];
        StringBuilder sb = new StringBuilder("");
        int len = 0;
        while ((len = input.read(temp)) > 0) {
            sb.append(new String(temp, 0, len));
        }
        input.close();
        return sb.toString();
    } catch (IOException e) {
        return "";
    }
}
//获取某个目录下的所有文件夹名和文件名
public List<String> getlist(File directory) {
        List<String> filenames = new ArrayList<>();
        if (directory != null && directory.exists() && directory.isDirectory()) {
            File[] files = directory.listFiles();
            if (files != null) {
                for (File file : files) {
                    filenames.add(file.getName());
                }
            }
        }
        return filenames;
    }
}