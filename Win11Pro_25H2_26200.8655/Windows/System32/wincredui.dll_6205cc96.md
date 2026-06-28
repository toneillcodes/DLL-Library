# Binary Specification: wincredui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wincredui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6205cc961d50852599ad5317da093b49a9e36749d1999146764528874011dfee`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CredUIInternalCmdLinePromptForCredentialsA` | `0x123D0` | 719 | UnwindData |  |
| 2 | `CredUIInternalCmdLinePromptForCredentialsW` | `0x126B0` | 94 | UnwindData |  |
| 3 | `CredUIInternalConfirmCredentialsA` | `0x12720` | 137 | UnwindData |  |
| 4 | `CredUIInternalConfirmCredentialsW` | `0x127B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CredUIInternalInitControls` | `0x127D0` | 42 | UnwindData |  |
| 6 | `CredUIInternalPromptForCredentialsA` | `0x12800` | 784 | UnwindData |  |
| 7 | `CredUIInternalPromptForCredentialsW` | `0x12B20` | 215 | UnwindData |  |
| 8 | `CredUIInternalPromptForWindowsCredentialsA` | `0x12C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CredUIInternalPromptForWindowsCredentialsW` | `0x12C10` | 382 | UnwindData |  |
| 10 | `CredUIInternalPromptForWindowsCredentialsWorker` | `0x12DA0` | 105 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x13670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllGetClassObject` | `0x13690` | 166 | UnwindData |  |
| 13 | `DllRegisterServer` | `0x13930` | 336 | UnwindData |  |
| 14 | `DllUnregisterServer` | `0x13A90` | 111 | UnwindData |  |
| 15 | `PasskeyOTSPrompt` | `0x13B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WHOTSLaunch` | `0x13B20` | 269 | UnwindData |  |
