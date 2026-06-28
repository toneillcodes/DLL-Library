# Binary Specification: ubpm.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ubpm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dd13c63d0c9f6c3c9d011c1ca885ef5708482269fe9ffe0c87f8905472abc8c2`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `UbpmTriggerConsumerUnregister` | `0x63E0` | 182 | UnwindData |  |
| 10 | `UbpmTriggerConsumerControl` | `0x6FF0` | 920 | UnwindData |  |
| 7 | `UbpmSessionStateChanged` | `0x7390` | 172 | UnwindData |  |
| 13 | `UbpmTriggerConsumerRegister` | `0x8480` | 256 | UnwindData |  |
| 5 | `UbpmOpenTriggerConsumer` | `0x9DF0` | 251 | UnwindData |  |
| 3 | `UbpmCloseTriggerConsumer` | `0x9F00` | 231 | UnwindData |  |
| 12 | `UbpmTriggerConsumerQueryStatus` | `0xC1B0` | 3,185 | UnwindData |  |
| 2 | `UbpmApiBufferFree` | `0x18530` | 66,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `UbpmTriggerConsumerSetStatePublishingSecurity` | `0x289C0` | 30 | UnwindData |  |
| 9 | `UbpmTriggerConsumerConfigure` | `0x2C2B0` | 958 | UnwindData |  |
| 8 | `UbpmTerminate` | `0x2FA30` | 461 | UnwindData |  |
| 4 | `UbpmInitialize` | `0x31540` | 257 | UnwindData |  |
| 1 | `UbpmAcquireJobBackgroundMode` | `0x34480` | 175 | UnwindData |  |
| 6 | `UbpmReleaseJobBackgroundMode` | `0x34540` | 157 | UnwindData |  |
| 11 | `UbpmTriggerConsumerControlNotifications` | `0x345F0` | 190 | UnwindData |  |
| 14 | `UbpmTriggerConsumerSetDisabledForUser` | `0x346C0` | 183 | UnwindData |  |
