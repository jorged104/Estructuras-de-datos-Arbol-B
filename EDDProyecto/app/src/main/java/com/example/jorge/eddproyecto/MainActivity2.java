package com.example.jorge.eddproyecto;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.Toast;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.concurrent.TimeUnit;

public class MainActivity2 extends AppCompatActivity {
    ImageView ImgQr;
    String usuario;
    Spinner lista;
    String[] datos ;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        usuario = getIntent().getExtras().getString("usuario");
        Button botonqr = (Button) findViewById(R.id.qr);
        Button botonArbolB = (Button) findViewById(R.id.arb);
        Button btmas = (Button) findViewById(R.id.bt_mas);
        //bhash
        Button ha = (Button) findViewById(R.id.bhash);
         ImgQr = (ImageView) findViewById(R.id.imageView2) ;
        lista = (Spinner) findViewById(R.id.spinner2);
        cargardatos();
        ArrayAdapter<String> adaptador = new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item,datos);
        lista.setAdapter(adaptador);
        botonqr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    SendRequest nuevo = new SendRequest("http://192.168.1.4:8080/cliente/llamarpython");
                    nuevo.addParam("tipo", "getQr");
                    nuevo.addParam("usuario", usuario);
                    nuevo.addParam("enemigo",(String)lista.getSelectedItem());
                    nuevo.execute();
                    nuevo.get(3000, TimeUnit.MILLISECONDS);
                    Toast.makeText(getApplicationContext(),nuevo.respuesta,
                            Toast.LENGTH_LONG).show();
                    byte[] decodedString = Base64.decode(nuevo.respuesta,Base64.NO_WRAP);
                    InputStream inputStream  = new ByteArrayInputStream(decodedString);
                    Bitmap bitmap  = BitmapFactory.decodeStream(inputStream);
                    ImgQr.setImageBitmap(bitmap);

                }catch (Exception e ){}
            }

        });
       Button boton2 = (Button) findViewById(R.id.botonmostrar);
        boton2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
        {
            mostrar();
        }
        });
        botonArbolB.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                arbolB();
            }
        });
        btmas.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                Intent ListSong = new Intent(MainActivity2.this, Mas.class);
                ListSong.putExtra("usuario",usuario);
                startActivity(ListSong);
            }
        });
        ha.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                graficarhash();
            }
        });
    }
    public void graficarhash(){
        try {
            SendRequest nuevo = new SendRequest("http://192.168.1.4:8080/cliente/llamarpython");
            nuevo.addParam("tipo", "graficarhash");

            nuevo.execute();
            nuevo.get(5000, TimeUnit.MILLISECONDS);
            Toast.makeText(getApplicationContext(),nuevo.respuesta,
                    Toast.LENGTH_LONG).show();
            byte[] decodedString = Base64.decode(nuevo.respuesta,Base64.NO_WRAP);
            InputStream inputStream  = new ByteArrayInputStream(decodedString);
            Bitmap bitmap  = BitmapFactory.decodeStream(inputStream);
            ImgQr.setImageBitmap(bitmap);

        }catch (Exception e ){}
    }
    public void arbolB(){
        try {
            SendRequest nuevo = new SendRequest("http://192.168.1.4:8080/cliente/llamarpython");
            nuevo.addParam("tipo", "graficarBP");

            nuevo.execute();
            nuevo.get(3000, TimeUnit.MILLISECONDS);
            Toast.makeText(getApplicationContext(),nuevo.respuesta,
                    Toast.LENGTH_LONG).show();
            byte[] decodedString = Base64.decode(nuevo.respuesta,Base64.NO_WRAP);
            InputStream inputStream  = new ByteArrayInputStream(decodedString);
            Bitmap bitmap  = BitmapFactory.decodeStream(inputStream);
            ImgQr.setImageBitmap(bitmap);

        }catch (Exception e ){}
    }
    public void cargardatos()
    {
        try {
            SendRequest nuevo = new SendRequest("http://192.168.1.4:8080/cliente/llamarpython");
            nuevo.addParam("tipo", "getListaEnemigos");
            nuevo.addParam("usuario", this.usuario);
            nuevo.execute();
            nuevo.get(3000, TimeUnit.MILLISECONDS);
            this.datos = nuevo.respuesta.split(",");
            Toast.makeText(getApplicationContext(),nuevo.respuesta,
                    Toast.LENGTH_LONG).show();
        }catch (Exception e ){}
    }
    public void mostrar()
    {
        try {
            SendRequest nuevo = new SendRequest("http://192.168.1.4:8080/cliente/llamarpython");
            nuevo.addParam("tipo", "getAvl");
            nuevo.addParam("usuario", usuario);
            nuevo.execute();
            nuevo.get(3000, TimeUnit.MILLISECONDS);
            Toast.makeText(getApplicationContext(),nuevo.respuesta,
                    Toast.LENGTH_LONG).show();
            byte[] decodedString = Base64.decode(nuevo.respuesta,Base64.NO_WRAP);
            InputStream inputStream  = new ByteArrayInputStream(decodedString);
            Bitmap bitmap  = BitmapFactory.decodeStream(inputStream);
            ImgQr.setImageBitmap(bitmap);

        }catch (Exception e ){}
    }
}
