# Binary Specification: credui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\credui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `299c634e3e73493a0ed12f0eae8d91547fd5b9e01ce96b6408b815f1f6f30832`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `CredUIConfirmCredentialsW` | `0x1310` | 60 | UnwindData |  |
| 20 | `CredUnPackAuthenticationBufferW` | `0x1DF0` | 83 | UnwindData |  |
| 14 | `CredUIPromptForWindowsCredentialsWorker` | `0x2830` | 182 | UnwindData |  |
| 2 | `CredPackAuthenticationBufferW` | `0x2910` | 270 | UnwindData |  |
| 13 | `CredUIPromptForWindowsCredentialsW` | `0x2E20` | 153 | UnwindData |  |
| 3 | `CredUICmdLinePromptForCredentialsA` | `0x49A0` | 153 | UnwindData |  |
| 4 | `CredUICmdLinePromptForCredentialsW` | `0x4A40` | 153 | UnwindData |  |
| 5 | `CredUIConfirmCredentialsA` | `0x4AE0` | 60 | UnwindData |  |
| 7 | `CredUIInitControls` | `0x4B30` | 37 | UnwindData |  |
| 10 | `CredUIPromptForCredentialsA` | `0x4B60` | 166 | UnwindData |  |
| 11 | `CredUIPromptForCredentialsW` | `0x4C10` | 166 | UnwindData |  |
| 12 | `CredUIPromptForWindowsCredentialsA` | `0x4CC0` | 153 | UnwindData |  |
| 1 | `CredPackAuthenticationBufferA` | `0xB4F0` | 29 | UnwindData |  |
| 19 | `CredUnPackAuthenticationBufferA` | `0xB4F0` | 29 | UnwindData |  |
| 8 | `CredUIParseUserNameA` | `0xB520` | 309 | UnwindData |  |
| 9 | `CredUIParseUserNameW` | `0xB660` | 91 | UnwindData |  |
| 15 | `CredUIReadSSOCredA` | `0xB6D0` | 457 | UnwindData |  |
| 16 | `CredUIReadSSOCredW` | `0xB8A0` | 318 | UnwindData |  |
| 17 | `CredUIStoreSSOCredA` | `0xB9F0` | 319 | UnwindData |  |
| 18 | `CredUIStoreSSOCredW` | `0xBB40` | 483 | UnwindData |  |
| 21 | `SspiGetCredUIContext` | `0xD7B0` | 503 | UnwindData |  |
| 22 | `SspiIsPromptingNeeded` | `0xD9B0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SspiPromptForCredentialsA` | `0xDB20` | 332 | UnwindData |  |
| 24 | `SspiPromptForCredentialsW` | `0xDC80` | 1,630 | UnwindData |  |
| 25 | `SspiUnmarshalCredUIContext` | `0xE2F0` | 797 | UnwindData |  |
| 26 | `SspiUpdateCredentials` | `0xE620` | 373 | UnwindData |  |
