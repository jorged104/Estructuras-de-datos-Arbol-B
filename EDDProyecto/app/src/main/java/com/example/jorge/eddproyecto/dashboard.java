package com.example.jorge.eddproyecto;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.concurrent.TimeUnit;

public class dashboard extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
        Button QR = (Button) findViewById(R.id.Qr);
        QR.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    SendRequest nuevo = new SendRequest("http://192.168.1.4:8080/cliente/llamarpython");
                    nuevo.addParam("tipo", "getusuarios");
                    nuevo.execute();
                    nuevo.get(1000, TimeUnit.MILLISECONDS);
                     Toast.makeText(getApplicationContext(),nuevo.respuesta,
                            Toast.LENGTH_LONG).show();

                }catch (Exception e ){}
            }

        });
    }
}
