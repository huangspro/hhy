package com.p2pmyself.app;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;
import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.HashMap;
import java.util.Map;
import org.json.*;
public class volleytool
{
    private Context context;

    public interface ResponseCallback
	{
        void onGetResponse(String message);
    }

    public volleytool(Context context)
	{
        this.context = context;
    }

    public void sendpost(String url, JSONObject json, final ResponseCallback callback)
	{
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
            Request.Method.GET,
            url,
            json,
            new Response.Listener<JSONObject>() {
                @Override
                public void onResponse(JSONObject response)
				{
                    try
					{
                        String message = response.getString("message");
                        if (callback != null)
						{
                            callback.onGetResponse(message);
                        }
                    }
					catch (JSONException e)
					{}
                }
            },
            new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error)
				{}
            }); Volley.newRequestQueue(context).add(jsonObjectRequest);
    }
public void sendget(String url) {//url如http://192.168.0.105:5000?username=hello
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
                Request.Method.GET,
                url,
                null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            String message = response.getString("message");
                            
                        } catch (Exception e) {}
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {}
                });
        Volley.newRequestQueue(context).add(jsonObjectRequest);
    }
}