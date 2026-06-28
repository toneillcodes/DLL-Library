# Binary Specification: netlogon.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netlogon.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `412f24dd12b61370a24df5859fe5872b5144425de67eaa9c24a1922e02d5a168`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DsrGetDcNameEx2` | `0x17000` | 1,580 | UnwindData |  |
| 14 | `I_NetNotifyDelta` | `0x1A430` | 49,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `I_NetLogonGetSerialNumber` | `0x26700` | 67 | UnwindData |  |
| 13 | `I_NetLogonSetServiceBits` | `0x26750` | 186 | UnwindData |  |
| 15 | `I_NetNotifyDsChange` | `0x26810` | 157 | UnwindData |  |
| 16 | `I_NetNotifyMachineAccount` | `0x26940` | 299 | UnwindData |  |
| 17 | `I_NetNotifyNetlogonDllHandle` | `0x26A80` | 105 | UnwindData |  |
| 18 | `I_NetNotifyNtdsDsaDeletion` | `0x26AF0` | 170 | UnwindData |  |
| 19 | `I_NetNotifyRole` | `0x26BA0` | 138 | UnwindData |  |
| 20 | `I_NetNotifyTrustedDomain` | `0x26C30` | 145 | UnwindData |  |
| 3 | `I_NetLogonAppendChangeLog` | `0x277A0` | 45 | UnwindData |  |
| 4 | `I_NetLogonCloseChangeLog` | `0x277E0` | 66 | UnwindData |  |
| 10 | `I_NetLogonNewChangeLog` | `0x27830` | 71 | UnwindData |  |
| 11 | `I_NetLogonReadChangeLog` | `0x27880` | 107 | UnwindData |  |
| 6 | `I_NetLogonGetAuthDataEx` | `0x367F0` | 1,006 | UnwindData |  |
| 12 | `I_NetLogonSendToSamOnDc` | `0x36BF0` | 1,262 | UnwindData |  |
| 23 | `NetILogonSamLogon` | `0x37160` | 112 | UnwindData |  |
| 22 | `NetIGetEncTypes` | `0x3C830` | 144 | UnwindData |  |
| 2 | `I_NetLogonAddressToSiteName` | `0x48320` | 216 | UnwindData |  |
| 21 | `InitSecurityInterfaceW` | `0x50240` | 34 | UnwindData |  |
| 9 | `I_NetLogonMixedDomain` | `0x614E0` | 87 | UnwindData |  |
| 5 | `I_NetLogonFree` | `0x6BC90` | 11,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `NlNetlogonMain` | `0x6E7E0` | 1,712 | UnwindData |  |
| 8 | `I_NetLogonLdapLookupEx` | `0x7EBA0` | 1,676 | UnwindData |  |
