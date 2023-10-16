# ai-tools-exam
**วัดพื้นฐานการเขียนโปรแกรม (45 คะแนน)**

5. (10 คะแนน) ตัวอย่างข้อมูล
    
    A = [{ time: ISODate(“2023-09-19”) }, { time: ISODate(“2023-02-19”) }, …]
    
    จากตัวอย่างข้อมูล A เป็น Array ที่มีขนาด 10,000,000 โดยที่ time จะถูกสุ่มโดยมี format ISODate และยังไม่ถูกเรียงลำดับ
    
    จงเขียน code ที่ใช้สำหรับ Sort จาก time น้อยไปมาก โดยให้มี Performance สูงที่สุด และใช้ Resource น้อยที่สุด
   
   <img width="682" alt="Screenshot 2566-10-13 at 17 11 34" src="https://github.com/porameht/ai-tools-exam/assets/89307294/3b1368f1-86ec-4e12-ac6e-2a798214f65f">


```
use chrono::{DateTime, Utc};

#[derive(Debug, PartialEq, Eq, Clone)]
struct MyData {
    time: DateTime<Utc>,
}

impl MyData {
    fn new(iso_date: &str) -> MyData {
        MyData {
            time: DateTime::parse_from_rfc3339(iso_date)
                .unwrap()
                .with_timezone(&Utc),
        }
    }
}

fn merge(left: Vec<MyData>, right: Vec<MyData>) -> Vec<MyData> {
    let mut result = Vec::with_capacity(left.len() + right.len());
    let (mut i, mut j) = (0, 0);

    while i < left.len() && j < right.len() {
        if left[i].time <= right[j].time {
            result.push(left[i].clone()); // Use clone()
            i += 1;
        } else {
            result.push(right[j].clone()); // Use clone()
            j += 1;
        }
    }

    result.extend_from_slice(&left[i..]);
    result.extend_from_slice(&right[j..]);
    result
}

fn parallel_merge_sort(arr: Vec<MyData>) -> Vec<MyData> {
    if arr.len() <= 1 {
        return arr;
    }

    let middle = arr.len() / 2;
    let (left, right) = arr.split_at(middle);

    let left = left.to_vec(); // Use to_vec() to clone the data
    let right = right.to_vec(); // Use to_vec() to clone the data

    let (left, right) = rayon::join(|| parallel_merge_sort(left), || parallel_merge_sort(right));

    merge(left, right)
}

fn main() {
    let a: Vec<MyData> = vec![
        MyData::new("2023-09-19T00:00:00Z"),
        MyData::new("2023-02-19T00:00:00Z"),
        // Add more data here following the same format
    ];

    let sorted_a = parallel_merge_sort(a);
    for item in &sorted_a {
        println!("{:?}", item);
    }
}
```
    
6. (10 คะแนน) จงบอกตัวอย่างของกราฟสำหรับ Linear Search และ Binary Search พร้อมอธิบายความแตกต่าง และอธิบายว่า Linear Search และ Binary Search เหมาะสมกับงานแบบใด

![download (1)](https://github.com/porameht/ai-tools-exam/assets/89307294/1ef79c66-758f-483f-927e-a4cb02f07646)

***Linear Search***
- เทียบค่าหรือเสิร์ชค่าไปทีละตัวตั้งแต่ index ตัวแรกจนถึง index ตัวสุดท้าย
- ข้อมูลใน Array หรือ List ที่ค้นหา ไม่จำเป็นต้องเป็นข้อมูลที่เรียงลำดับหรือไม่เรียงลำดับ (Sorted Numbers or Unsorted Numbers) ก็คือจะ sort หรือไม่ sort ก็ได้
- ประสิทธิภาพเมื่อเทียบกับเวลา (Time Complexity) คือ O(n)
- เป็นเสิร์ชอัลกอริทึมที่เรียบง่ายที่สุด
- เหมาะสำหรับการค้นหาในข้อมูลขนาดเล็กหรือไม่เรียงลำดับ

**Binary Search**
- ในอัลกอริทึม binary search การค้นหาจะเริ่มที่ตรงกลางของช่วงข้อมูลและเปรียบเทียบค่าที่ต้องการค้นหากับค่ากลาง ถ้าค่าที่ต้องการมากกว่าค่ากลางจะค้นหาในครึ่งขวาของช่วงข้อมูล และถ้าน้อยกว่าจะค้นหาในครึ่งซ้าย
- ข้อมูลที่ใช้ในการค้นหาจะต้องเรียงลำดับ (Sorted Numbers) มาก่อน
- ประสิทธิภาพเมื่อเทียบกับเวลา (Time Complexity) คือ O(log n) ซึ่งเร็วกว่ามากเมื่อเทียบกับ linear search
- Binary search เหมาะสำหรับการค้นหาในข้อมูลที่มีขนาดใหญ่และเรียงลำดับ
- เหมาะสำหรับการค้นหาในข้อมูลที่เรียงลำดับและใหญ่

7. (25 คะแนน) จงสร้าง Web สำหรับ CRUD โดยใช้ AI ในการเขียน Code พร้อมทั้งใช้ Docker ให้ผู้ตรวจข้อสอบสามารถรันและใช้งานระบบได้

   Generate API Spec
   ```
   prompt: Generate API Spec for the following requirement:
   ```
   Result: Can test code this => `https://editor.swagger.io/`

   this project CRUD generate => `https://github.com/porameht/rust-ai-generate-crud`
   this conversetion history => `https://chat.openai.com/share/f52094ae-e32c-440b-a9e1-0da6b235e2b7`
