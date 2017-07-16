package com.example.jorge.eddproyecto;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.concurrent.TimeUnit;

public class Mas extends AppCompatActivity {
String usuario;
EditText contacto;
EditText newpass;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mas);
        usuario = getIntent().getExtras().getString("usuario");
        contacto = (EditText)findViewById(R.id.contactoText);
        newpass = (EditText)findViewById(R.id.pass);
        Button boton2 = (Button) findViewById(R.id.buttonE);
        boton2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                eliminarC();
            }
        });
        Button boton3 = (Button) findViewById(R.id.btpass);
        boton3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                modificar();
            }
        });
    }
    public void eliminarC()
    {
        try {
            SendRequest nuevo = new SendRequest("http://192.168.1.4:8080/cliente/llamarpython");
            nuevo.addParam("tipo", "eliminarContacto");
            nuevo.addParam("usuario", this.usuario);
            nuevo.addParam("contacto",this.contacto.getText().toString() );
            nuevo.execute();
            nuevo.get(3000, TimeUnit.MILLISECONDS);
            Toast.makeText(getApplicationContext(),nuevo.respuesta,
                    Toast.LENGTH_LONG).show();
        }catch (Exception e ){}
    }
    public void modificar()
    {
        try {
            SendRequest nuevo = new SendRequest("http://192.168.1.4:8080/cliente/llamarpython");
            nuevo.addParam("tipo", "modificarContacto");
            nuevo.addParam("usuario", this.usuario);
            nuevo.addParam("contacto",this.contacto.getText().toString() );
            nuevo.addParam("nuevapass",this.newpass.getText().toString() );
            nuevo.execute();
            nuevo.get(3000, TimeUnit.MILLISECONDS);
            Toast.makeText(getApplicationContext(),nuevo.respuesta,
                    Toast.LENGTH_LONG).show();
        }catch (Exception e ){}
    }
}
