use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex::Regex;

fn main() -> io::Result<()> {
    let path = Path::new("/Users/olivernormand/Documents/GitHub/advent_of_code/inputs/2.txt");
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);

    // Regex to find integers
    let _re = Regex::new(r"\d").unwrap();

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split(":").collect();

        for part in parts.iter() {
            let subparts: Vec<&str> = part.split(';').map(|s| s.trim()).collect();
            println!("{:?}", subparts)
        }
    }

    Ok(())
}

