# Binary Specification: wincredui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wincredui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `741d6b578d83041bd5e6b2ff22728f425e54cf26473bea5d863b8a6cdab10532`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CredUIInternalCmdLinePromptForCredentialsA` | `0x13C00` | 719 | UnwindData |  |
| 2 | `CredUIInternalCmdLinePromptForCredentialsW` | `0x13EE0` | 94 | UnwindData |  |
| 3 | `CredUIInternalConfirmCredentialsA` | `0x13F50` | 137 | UnwindData |  |
| 4 | `CredUIInternalConfirmCredentialsW` | `0x13FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CredUIInternalInitControls` | `0x14000` | 42 | UnwindData |  |
| 6 | `CredUIInternalPromptForCredentialsA` | `0x14030` | 784 | UnwindData |  |
| 7 | `CredUIInternalPromptForCredentialsW` | `0x14350` | 215 | UnwindData |  |
| 8 | `CredUIInternalPromptForWindowsCredentialsA` | `0x14430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CredUIInternalPromptForWindowsCredentialsW` | `0x14440` | 382 | UnwindData |  |
| 10 | `CredUIInternalPromptForWindowsCredentialsWorker` | `0x145D0` | 105 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x14EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllGetClassObject` | `0x14EC0` | 166 | UnwindData |  |
| 13 | `DllRegisterServer` | `0x15160` | 336 | UnwindData |  |
| 14 | `DllUnregisterServer` | `0x152C0` | 111 | UnwindData |  |
| 15 | `PasskeyOTSPrompt` | `0x15340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WHOTSLaunch` | `0x15350` | 269 | UnwindData |  |
