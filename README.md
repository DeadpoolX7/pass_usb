pass_usb: USB Password Manager
===============================

**pass_usb** is a Python-based USB password manager that enables users to securely store and retrieve their passwords using a USB device. This tool ensures that your sensitive information remains portable and accessible only when the designated USB device is connected to your system.

Features
--------

*   **Secure Storage**: Encrypts passwords and stores them on your USB device, ensuring data safety.
    
*   **Portability**: Access your passwords on any system by simply connecting your USB device.
    
*   **User Authentication**: Ensures that only authorized users can access the stored passwords.
    

Prerequisites
-------------

Before using pass_usb, ensure you have the following:

*   **Python 3.x**: The script is written in Python and requires Python 3.x to run.
    
*   **USB Device**: A USB flash drive to store and retrieve your encrypted passwords.
    
*   ```bash
    pip install cryptography sqlite3
    ```

Installation
------------

1.  ```bash
    git clone https://github.com/DeadpoolX7/pass_usb.git
    ```
2.  **Prepare Your USB Device**:
    
    *   Insert your USB flash drive into your computer.
        
    *   Note the mount point or drive letter assigned to your USB device.
        
3.  **Open terminal**
  - Run:
    ```bash
    python pass_boss.py
    ```
4.  Execute the script using Python:
```bash
pass_boss.py
```    

Usage
-----

Upon running the script, you'll be presented with a menu to manage your passwords:

1.  **Add a New Password**: Store a new password entry on your USB device.
    
2.  **Retrieve a Password**: Access and decrypt a stored password.
    
3.  **Delete a Password**: Remove an existing password entry.
    
4.  **List All Entries**: View all stored password entries.
    
5.  **Exit**: Close the application.
    

**Note**: Ensure your USB device is connected at all times while using the application. The script reads from and writes to the USB device directly.

Security Considerations
-----------------------

*   **Encryption**: The script utilizes the cryptography library to encrypt and decrypt your passwords, ensuring they are stored securely on the USB device.
    
*   **USB Safety**: Always eject your USB device safely to prevent data corruption.
    
*   **Backup**: Regularly back up your encrypted password file to prevent data loss in case the USB device is damaged or lost.
    

License
-------

This project is licensed under the MIT License. See the [LICENSE](https://github.com/DeadpoolX7/pass_usb/blob/main/LICENSE) file for more details.

Acknowledgments
---------------

Special thanks to [Sanju Shaw](https://github.com/DeadpoolX7) for developing this tool.
