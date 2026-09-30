#![allow(static_mut_refs)]
use std::io::{BufWriter, Stdout, Write};
static mut STDOUT: Option<BufWriter<Stdout>> = None;
macro_rules! println { ($($t:tt)*) => { unsafe { writeln!(STDOUT.as_mut().unwrap_unchecked(), $($t)*).unwrap_unchecked() } }; }

fn string() -> &'static str {
    let s = std::io::read_to_string(std::io::stdin()).unwrap();
    Box::leak(s.into_boxed_str())
}

fn words() -> impl Iterator<Item = &'static str> {
    let s = string();
    s.split_ascii_whitespace()
}

fn main() {
    unsafe {
        STDOUT = Some(BufWriter::with_capacity(1 << 17, std::io::stdout()));
        solve();
        STDOUT.as_mut().unwrap_unchecked().flush().ok();
    }
}

fn solve() {
    let mut it = words().map(|x| x.parse::<isize>().unwrap());
    let t = it.next().unwrap();
    for _ in 0..t {
        let n = it.next().unwrap() as usize;
        let mut min1 = isize::MAX;
        let mut min2 = isize::MAX;
        let mut max1 = isize::MIN;
        let mut max2 = isize::MIN;
        for x in it.by_ref().take(n) {
            if x < min1 {
                (min1, min2) = (x, min1);
            } else if x < min2 {
                min2 = x;
            }

            if x > max1 {
                (max1, max2) = (x, max1);
            } else if x > max2 {
                max2 = x;
            }
        }
        let ans = (max1 * max2).max(min1 * min2);
        println!("{ans}");
    }
}