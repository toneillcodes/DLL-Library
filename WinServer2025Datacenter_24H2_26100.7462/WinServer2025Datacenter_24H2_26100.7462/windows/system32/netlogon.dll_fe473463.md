# Binary Specification: netlogon.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netlogon.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fe473463a1693150134e63104ed9b97e5856044a9e3589a43c991b1b973a04ef`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DsrGetDcNameEx2` | `0x17580` | 1,580 | UnwindData |  |
| 14 | `I_NetNotifyDelta` | `0x1A9B0` | 48,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `I_NetLogonGetSerialNumber` | `0x266B0` | 67 | UnwindData |  |
| 13 | `I_NetLogonSetServiceBits` | `0x26700` | 186 | UnwindData |  |
| 15 | `I_NetNotifyDsChange` | `0x267C0` | 157 | UnwindData |  |
| 16 | `I_NetNotifyMachineAccount` | `0x268F0` | 299 | UnwindData |  |
| 17 | `I_NetNotifyNetlogonDllHandle` | `0x26A30` | 105 | UnwindData |  |
| 18 | `I_NetNotifyNtdsDsaDeletion` | `0x26AA0` | 170 | UnwindData |  |
| 19 | `I_NetNotifyRole` | `0x26B50` | 138 | UnwindData |  |
| 20 | `I_NetNotifyTrustedDomain` | `0x26BE0` | 145 | UnwindData |  |
| 3 | `I_NetLogonAppendChangeLog` | `0x276D0` | 45 | UnwindData |  |
| 4 | `I_NetLogonCloseChangeLog` | `0x27710` | 66 | UnwindData |  |
| 10 | `I_NetLogonNewChangeLog` | `0x27760` | 71 | UnwindData |  |
| 11 | `I_NetLogonReadChangeLog` | `0x277B0` | 107 | UnwindData |  |
| 6 | `I_NetLogonGetAuthDataEx` | `0x35B80` | 1,006 | UnwindData |  |
| 12 | `I_NetLogonSendToSamOnDc` | `0x35F80` | 1,262 | UnwindData |  |
| 23 | `NetILogonSamLogon` | `0x364F0` | 112 | UnwindData |  |
| 22 | `NetIGetEncTypes` | `0x3CA90` | 144 | UnwindData |  |
| 2 | `I_NetLogonAddressToSiteName` | `0x48580` | 216 | UnwindData |  |
| 21 | `InitSecurityInterfaceW` | `0x504A0` | 34 | UnwindData |  |
| 9 | `I_NetLogonMixedDomain` | `0x61740` | 87 | UnwindData |  |
| 5 | `I_NetLogonFree` | `0x6BDB0` | 11,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `NlNetlogonMain` | `0x6E900` | 1,775 | UnwindData |  |
| 8 | `I_NetLogonLdapLookupEx` | `0x7EC50` | 1,676 | UnwindData |  |
