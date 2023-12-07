use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex::Regex;

fn main() -> io::Result<()> {
    let path = Path::new("/Users/olivernormand/Documents/GitHub/advent_of_code/inputs/1.txt");
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);
    let mut total: i32 = 0;

    // Regex to find integers
    let re = Regex::new(r"\d").unwrap();

    for line in reader.lines() {
        let line = line?;

        // Find all matches and parse them as integers
        let numbers: Vec<i32> = re.find_iter(&line)
                                  .filter_map(|digit| digit.as_str().parse().ok())
                                  .collect();

        let x: i32 = calibration_value(&numbers);
        println!("{:?} {:?}", numbers, x);
        total = total + x

        // Now, 'numbers' is a vector of integers found in the line
        // You can add your additional logic here
    }

    println!("{:?}", total);
    Ok(())
}

fn calibration_value(numbers: &[i32]) -> i32 {
    let first = numbers.first().unwrap();
    let last = numbers.last().unwrap();
    first * 10 + last
} 
