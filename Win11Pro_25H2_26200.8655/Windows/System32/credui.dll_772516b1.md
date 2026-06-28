# Binary Specification: credui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\credui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `772516b1281a5deccc4494b6579a9080fab18c6bee6ec2e3297b8a46389a38ee`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `CredUIConfirmCredentialsW` | `0x1300` | 60 | UnwindData |  |
| 20 | `CredUnPackAuthenticationBufferW` | `0x1E70` | 83 | UnwindData |  |
| 14 | `CredUIPromptForWindowsCredentialsWorker` | `0x2750` | 182 | UnwindData |  |
| 2 | `CredPackAuthenticationBufferW` | `0x2830` | 270 | UnwindData |  |
| 13 | `CredUIPromptForWindowsCredentialsW` | `0x33B0` | 153 | UnwindData |  |
| 3 | `CredUICmdLinePromptForCredentialsA` | `0x4F40` | 153 | UnwindData |  |
| 4 | `CredUICmdLinePromptForCredentialsW` | `0x4FE0` | 153 | UnwindData |  |
| 5 | `CredUIConfirmCredentialsA` | `0x5080` | 60 | UnwindData |  |
| 7 | `CredUIInitControls` | `0x50D0` | 37 | UnwindData |  |
| 10 | `CredUIPromptForCredentialsA` | `0x5100` | 166 | UnwindData |  |
| 11 | `CredUIPromptForCredentialsW` | `0x51B0` | 166 | UnwindData |  |
| 12 | `CredUIPromptForWindowsCredentialsA` | `0x5260` | 153 | UnwindData |  |
| 1 | `CredPackAuthenticationBufferA` | `0xBA20` | 29 | UnwindData |  |
| 19 | `CredUnPackAuthenticationBufferA` | `0xBA20` | 29 | UnwindData |  |
| 8 | `CredUIParseUserNameA` | `0xBA50` | 309 | UnwindData |  |
| 9 | `CredUIParseUserNameW` | `0xBB90` | 91 | UnwindData |  |
| 15 | `CredUIReadSSOCredA` | `0xBC00` | 457 | UnwindData |  |
| 16 | `CredUIReadSSOCredW` | `0xBDD0` | 318 | UnwindData |  |
| 17 | `CredUIStoreSSOCredA` | `0xBF20` | 319 | UnwindData |  |
| 18 | `CredUIStoreSSOCredW` | `0xC070` | 483 | UnwindData |  |
| 21 | `SspiGetCredUIContext` | `0xDB90` | 503 | UnwindData |  |
| 22 | `SspiIsPromptingNeeded` | `0xDD90` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SspiPromptForCredentialsA` | `0xDF00` | 332 | UnwindData |  |
| 24 | `SspiPromptForCredentialsW` | `0xE060` | 1,630 | UnwindData |  |
| 25 | `SspiUnmarshalCredUIContext` | `0xE6D0` | 797 | UnwindData |  |
| 26 | `SspiUpdateCredentials` | `0xEA00` | 373 | UnwindData |  |
