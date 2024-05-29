using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Collections.Specialized;
using System.Security.Cryptography;
using System.Text;
using MySql.Data.MySqlClient;
using System.Data.SQLite;
using Newtonsoft.Json;

namespace app;

public class SQLRequest
{
    // Connection à la base de données ------------------------------------------------------------------------------------------------------
    public static MySqlConnection OpenBDDConnection()
    {
        // string connectionString = "Data Source=chemin_de_la_database";
        // string connectionString = @"Data Source=../BDD_Projet_Final_B2/Database_Biblio.db"; // Chemin relatif
        string connectionString = $"serve=172.16.238.10;port=3306;User ID=root;Password=root;";


        try
        {
            // Création de la connection
            MySqlConnection connection = new MySqlConnection(connectionString);
            // Ouverture de la connection avec la base de données
            connection.Open();
            Console.WriteLine("Connexion réussie à la base de données MySql!");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Erreur de connexion: " + ex.Message);
        }
        return connection;
    }

    public static dynamic ExecuteSelectQuery(MySqlConnection connection, string query)
    {
        DataTable dataTable = new DataTable();
        // Console.WriteLine(query);
        using (MySqlCommand command = new MySqlCommand(query, connection))
        using (MySqlDataAdapter adapter = new MySqlDataAdapter(command))
        {
            adapter.Fill(dataTable);
        }

        string jsonResult = JsonConvert.SerializeObject(dataTable, Formatting.Indented);
        return JsonConvert.DeserializeObject(jsonResult);
    }

    public static void ExecuteOtherQuery(MySqlConnection connection, string query)
    {
        MySqlCommand command = new MySqlCommand(query, connection);
        int rowsAffected = command.ExecuteNonQuery();
    }
}