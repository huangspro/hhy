//该类用于生成json对象,如m("h","u")
//将会生成{"h":"u"}
package com.volley.app;

import org.json.JSONObject;

public class jsonhelp {
    public static JSONObject m(String... keyValuePairs) {
        JSONObject jsonObject = new JSONObject();
        try {
            for (int i = 0; i < keyValuePairs.length; i += 2) {
                jsonObject.put(keyValuePairs[i], keyValuePairs[i + 1]);
            }
            return jsonObject;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}