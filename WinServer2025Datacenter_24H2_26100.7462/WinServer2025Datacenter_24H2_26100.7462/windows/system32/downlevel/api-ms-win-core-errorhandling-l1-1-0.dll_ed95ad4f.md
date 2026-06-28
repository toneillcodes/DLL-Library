# Binary Specification: api-ms-win-core-errorhandling-l1-1-0.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\downlevel\api-ms-win-core-errorhandling-l1-1-0.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ed95ad4f623869809885b19e5178bc67bee5ecc9f3aacae6980c869abec992ea`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetErrorMode` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetErrorMode` |
| 2 | `GetLastError` | `0x0` | - | Forwarded | Forwarded to: `kernel32.GetLastError` |
| 3 | `RaiseException` | `0x0` | - | Forwarded | Forwarded to: `kernel32.RaiseException` |
| 4 | `SetErrorMode` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetErrorMode` |
| 5 | `SetLastError` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetLastError` |
| 6 | `SetUnhandledExceptionFilter` | `0x0` | - | Forwarded | Forwarded to: `kernel32.SetUnhandledExceptionFilter` |
| 7 | `UnhandledExceptionFilter` | `0x0` | - | Forwarded | Forwarded to: `kernel32.UnhandledExceptionFilter` |
