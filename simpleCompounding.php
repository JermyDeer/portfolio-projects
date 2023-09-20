<?php

/*This code will calculate the compound interest 
annually given time, interest rate, and 
capital to invest. Results displayed in a simple chart. */

//function to calculate compound interest
function compoundCalc($interest, $capital, $time = 1)
{
    $chart = array([$capital, $interest, $time]);
    for ($y = 0; $y < $time; $y++) {
        $capital += 20000;
        $capital = $capital * (1 + $interest);
        $chart[] = $capital;
    }
    return $chart;
}

//function to display results
function displayResult($array)
{
    $capital = $array[0][0];
    $interest = $array[0][1] * 100;
    $time = $array[0][2];

    echo "\n";
    echo "The compounded return on $" 
    . number_format($capital, 2) 
    . " at " 
    . $interest . "% interest for " 
    . $time . " years is: $" 
    . number_format($array[$time], 2);
    echo "\n";
}

//function to compare different results
function compareResult()
{
    $table = func_get_args();

    foreach ($table as $result){
        displayResult($result);
    }

    //var_dump($table);
    return $table;
}
    
//function to show comparison table
function displayTable($tables)
{
    //Table Header printing
    print("\n------------------------------------------------\n");
    $header = "|";
    $header .= str_pad($header, 3, " ", STR_PAD_LEFT);
    foreach ($tables as $table){
        $header .= str_pad($table[0][1], 14, " ", STR_PAD_BOTH) . "|";
    }
    echo $header;
    print("\n-------------------------------------------------");

    //Table Rows printing

    for ($i = 1; $i <= $tables[0][0][2]; $i++){
        $row = "\n";
        $row .= str_pad("$i.| ", 5, " ", STR_PAD_LEFT);
        foreach ($tables as $table){
            $row .= str_pad(number_format($table[$i], 2)
            , 18 - strlen(round($table[$i]))
            , " "
            , STR_PAD_LEFT);
            $row .= " | ";
        }
        echo $row;
    }      
}

//Function add cash to capital  periodically
function addCash($amount = 0)
{
    $capital = $amount;
    return $capital;
}



$capital = 100000;
$stock_int = 0.11;
$mutual_int = 0.08;
$house_int = 0.06;

$time = 30;


$returnOne = compoundCalc($stock_int, $capital, $time);
$returnThree = compoundCalc($mutual_int, $capital, $time);
$returnTwo = compoundCalc($house_int, $capital, $time);
$table = compareResult($returnOne, $returnThree, $returnTwo);

displayTable($table);
//displayResult($return);
