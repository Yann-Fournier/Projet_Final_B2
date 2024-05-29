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
        string connectionString = $"server=172.16.238.10;port=3306;User ID=root;Password=root;";

        bool isConnected = false;

        while !isConnected {
            // Création de la connection
            MySqlConnection connection = new MySqlConnection(connectionString);
            try
            {
                // Ouverture de la connection avec la base de données
                connection.Open();
                Console.WriteLine("Connexion réussie à la base de données MySql!");
                isConnected = true;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Erreur de connexion: " + ex.Message);
            }
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

    public static String HashPwd(string mdp)
    {
        using (SHA256Managed sha1 = new SHA256Managed())
        {
            var hash = sha1.ComputeHash(Encoding.UTF8.GetBytes(mdp));
            var sb = new StringBuilder(hash.Length * 2);

            foreach (byte b in hash)
            {
                // can be "x2" if you want lowercase
                sb.Append(b.ToString("X2"));
            }

            return sb.ToString();
        }
    }
}