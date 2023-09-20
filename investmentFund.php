<?php

//Get percent weight of stock. Get Total fund capital. Get Dollar value of weight for stock. Get Share number for dollar weight. Approximate number to buy. 

//function to create daily return data
function returnTable($stocks) 
{
    $a = 0;
    foreach ($stocks as $stock){
        $a++;
    }
    for ($i = 1; $i < $a; $i++){
        $volatility = $stocks[$i][2];
        $dailyReturn = $volatility * (rand(-100, 100) / 100.0);
        echo "\n" . $dailyReturn;
    }
}

//Function to calculate sum of items
function sumStocks($stocks, $num)
{
    $capital = $stocks[0][1];
    $sum = 0;
    for ($i = 1; $i < $num; $i++){

        $stockName = $stocks[$i][0];
        echo "\n----- ".$stockName." -----";

        $stockPrice = $stocks[$i][1];
        echo "\n Stock Price: ".$stockPrice;

        $stockVolatility = $stocks[$i][2];
        echo "\n Stock Volatility: ".$stockVolatility;

        $stockWeight = $stocks[$i][3];
        echo "\n Stock Weight: ".$stockWeight;

        $allocationDollars = $capital * $stockWeight;
        echo "\n Stock Allocation Dollars: ". $allocationDollars;

        $numStocks = $allocationDollars / $stockPrice;
        echo "\n Number of Stocks: " . $numStocks;
        echo "\n--------------------";

        $sum += $allocationDollars;
    }
    echo "\n Sum total of all stocks in portfolio : " . $sum;

}

//Function to Calculate Fund Volatility
function fundVolatility()
{

}

//Function to rebalance fund
function rebalance($stocks)
{
    $targetVolatility = $stocks[0][2] / 100; //Target of fund
    $fundCapital = $stocks[0][1];

    $count = 0; //Counter for number of stocks in array
    foreach ($stocks as $stock){
        $count++;
    }

    $weights = array(); //Array of target weights from stocks
    for ($i = 1; $i < $count; $i++){
        $weights[] = $targetVolatility / $stocks[$i][2];
        // echo "\n".$weights[$i-1];
    }
    $weightSum = array_sum($weights);
    // echo "\n==========================";
    // echo "\n".$weightSum;
    // echo "\n==========================";

    //Normalize weights as percentage of total capital in fund
    for ($i = 0; $i < $count-1; $i++){
        $weights[$i] = $weights[$i] / $weightSum;
        $stocks[$i+1][3] = $weights[$i];
        // echo "\n". $i+1 . ": ".$stocks[$i+1][3];
    }

    //Get dollar weight for each stock
    // for ($i = 0; $i < $count-1; $i++){
    //     $weights[$i] = $weights[$i] * $fundCapital;
    //     echo "\n". $i+1 . ": ".$weights[$i];
    // }
    return $stocks;
    
}

//Function to display securities, and weights

//Function to initialize fund
//[0] position of array is the fund name
//all following the stock names
function fundInit($fundCapital = 100000, $fundName = "Capital GAINZ", $stocksNum = 10, $targetVolatility = 11)
{
    $fund = array();
    $fund[] = array($fundName, $fundCapital, $targetVolatility);

    for ($i = 0; $i < $stocksNum; $i++){
        $fund[] = makeStock($stocksNum);
    }
    return $fund;
}

//Function to produce random stock/security
function makeStock($stocksNum)
{
    $stockPrice = random_int(1, 500);
    $stockName = "STK: " . $stockPrice;
    $stockVolatility = rand(3, 25) / 100;
    $stockWeight = 1 / $stocksNum;
    $stock = array($stockName, $stockPrice, $stockVolatility, $stockWeight);
    return $stock;
}

$result = fundInit();

$result = rebalance($result);

//returnTable($result);
var_dump($result);
//$sum = sumStocks($result, 11);
