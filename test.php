<?php // script principale

// stampa un messaggio
echo "HELLO WORLD";

// definizione di variabili
$nome = "Marco";
$eta = 20;

// concatenazione di stringhe e stampa
echo $nome . " ha " . $eta . " anni.";

// stampa il tipo di dato
var_dump($eta);

// creazione di un array e stampa elementi
$frutti = ['mela', 'pera', 'banana'];
foreach ($frutti as $f) {
    echo $f . "<br>";
}

// creazione di un array associativo e stampa elemento
$user = [
    'nome' => 'Luca',
    'email' => 'luca@example.com'
];
echo $user['email'];

// definizione di una funzione con parametri facoltativi
function somma($a, $b = 0) {
    return $a + $b;
}

// chiamata alla funzione e stampa risultato
echo somma(2, 3); // 5

// formulario HTML e gestione della submit
?>
<form method="post" action="submit.php">
  <input name="username">
  <button>Invia</button>
</form>

<?php
// gestione della submit
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'] ?? '';
    echo "Ciao " . htmlspecialchars($username, ENT_QUOTES);
}
?>

<?php // lettura e scrittura su file

$content = file_get_contents('dati.txt');
file_put_contents('dati2.txt', $content . "\nnuova riga");
?>

<?php // uso di sessioni

session_start();
$_SESSION['user'] = 'marco';
echo $_SESSION['user'];
?>

<?php // creazione di un oggetto

// creazione di una classe "Persona" con un attributo privato e un metodo pubblico
class Persona {
  private $nome; // attributo privato
  public function __construct($n){ $this->nome = $n; } // costruttore che imposta il nome
  public function saluta(){ return "Ciao " . $this->nome; } // metodo pubblico che restituisce il saluto
}

// creazione di un oggetto "Persona" con il nome "Anna"
$p = new Persona("Anna");

// chiamata del metodo pubblico "saluta" dell'oggetto $p e stampa il risultato
echo $p->saluta();
?>

<?php
// connessione al database
$mysqli = mysqli_connect('localhost','user','pass','db');

// esecuzione di una query e iterazione sui risultati
$result = mysqli_query($mysqli, "SELECT * FROM users");
while($row = mysqli_fetch_assoc($result)){
  echo $row['email'] . "<br>"; // stampa l'email di ogni utente
}
?>

<?php
// esecuzione di una query e iterazione sui risultati
$mysqli = mysqli_connect('localhost','user','pass','db');
$result = mysqli_query($mysqli, "SELECT * FROM users");
while($row = mysqli_fetch_assoc($result)){
  echo $row['email'] . "<br>"; // stampa l'email di ogni utente
}
?>
