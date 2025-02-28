Title: Blogging - Intro
Author: Julz
Date: 2025-01-17
Category: Learning, rust, programming
Tags: Programming, Rust, Learning

Learning Rust. 

Rust
---
Notes

* [lunch and learn - rust book/video](https://learning.oreilly.com/videos/learn-rust-in/9781633438231VE/)
* 'the hangover before the party'
* https://www.reddit.com/r/rust/comments/1ift6e5/python_developer_getting_started_with_rust/
  * https://rust-exercises.com/100-exercises-to-learn-rust.pdf
* Rust to pip : https://medium.com/towards-data-science/how-to-make-your-python-packages-really-fast-with-rust-91a9bebacbc2 with [maturin](https://www.maturin.rs) : smooth out rust to python 
  integration! OMG!
* I have a project in mind: eg something like: [DSP sound synth with rust](https://www.youtube.com/watch?v=R6v96c-ahAM); or [this synth](https://github.com/vitobasso/rust-synth) 

Rust Primer
---

New to rust? here's a cheat sheet.


Start with the basics: Comments & docs
---
```Rust
 // hello world - comment line
 /* hello world ! */ 
 /// doc comments like this /// 
```
* `cargo doc --open` : to make the documentation site (awesome!)

Now we can write a comment or two, let's make variables! 

Variables
---

### Primitives

* signed integers i8 i16 i32 i64 i128 isize
* unsigned integers u8 u16 u32 u64 u128 usize
* i8 up to 255; u16 up to 16000 (and a bit!
* chars : `println!("len {}  ", "ç".len())` returns '2' not '1' : number of bytes, not characters)
* println!("chars {:?}  ", "a".as_bytes()); gives the bytes of the string
* println!("chars count {}  ", "aaaà".chars().count()); gives the number of characters in the string

### Type inference

 `let my_number = 10:u8;` // type after the value
 `let my_number:u8 = 10;` // type with the variable
 `let my_number = 10_000_000_i32;` // type with formatting
 
### Mutability

By default immutable:

* `let const = 1;` // immutable
* `let mut var = 1;` // mutable
* `var= "one";` // error: expected integer, found `&str`

### Shadowing

Scope, re-declaring variables, and shadowing:

* In the same block:
```Rust
  let x = 5;
  let x = 5.1; // shadowing
  println!("The value of x is: {}", x); // 5.1
```
In separate blocks:
```Rust
let x = 5;
  {
  let x = 6.1;
  println!("The value of x is: {}", x); // 6.1
 }
 println!("The value of x is: {}", x); // 5
```

### Constants

* `const MAX_POINTS: u32 = 100_000;` // must be annotated

### Data types

* `let x = 2.0;` // assumes f64
* `let y: f32 = 3.0;` // explicitly f32
