use std::env;
use std::fs;
use std::io;
use std::path::Path;

fn main() -> io::Result<()> {
    // 获取当前工作目录
    let current_dir = env::current_dir()?;
    
    // 读取目录内容
    let entries = fs::read_dir(&current_dir)?;
    
    println!("当前目录: {}", current_dir.display());
    println!("{:-<40}", ""); // 分隔线
    
    // 遍历并打印所有条目
    for entry in entries {
        let entry = entry?;
        let path = entry.path();
        
        // 获取文件名
        let name = path.file_name()
            .and_then(|n| n.to_str())
            .unwrap_or("Invalid filename");
        
        // 判断是文件还是目录
        let entry_type = if path.is_dir() {
            "目录"
        } else if path.is_file() {
            "文件"
        } else {
            "其他"
        };
        
        // 获取文件大小（如果是文件）
        let size = if path.is_file() {
            format!("{} bytes", path.metadata()?.len())
        } else {
            "".to_string()
        };
        
        println!("[{}] {:20} {}", entry_type, name, size);
    }
    
    Ok(())
}
