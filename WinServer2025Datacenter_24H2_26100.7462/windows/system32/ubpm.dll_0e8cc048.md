# Binary Specification: ubpm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ubpm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0e8cc048ce1be81f7697d671946ab9363f24d1c1e29ceb8d09705d32d6159dd4`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `UbpmTriggerConsumerUnregister` | `0x63D0` | 182 | UnwindData |  |
| 10 | `UbpmTriggerConsumerControl` | `0x6FE0` | 920 | UnwindData |  |
| 7 | `UbpmSessionStateChanged` | `0x7380` | 172 | UnwindData |  |
| 13 | `UbpmTriggerConsumerRegister` | `0x8470` | 256 | UnwindData |  |
| 5 | `UbpmOpenTriggerConsumer` | `0x9DE0` | 251 | UnwindData |  |
| 3 | `UbpmCloseTriggerConsumer` | `0x9EF0` | 231 | UnwindData |  |
| 12 | `UbpmTriggerConsumerQueryStatus` | `0xC1A0` | 3,185 | UnwindData |  |
| 2 | `UbpmApiBufferFree` | `0x18520` | 66,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `UbpmTriggerConsumerSetStatePublishingSecurity` | `0x289B0` | 30 | UnwindData |  |
| 9 | `UbpmTriggerConsumerConfigure` | `0x2C2A0` | 958 | UnwindData |  |
| 8 | `UbpmTerminate` | `0x2FA20` | 461 | UnwindData |  |
| 4 | `UbpmInitialize` | `0x31530` | 257 | UnwindData |  |
| 1 | `UbpmAcquireJobBackgroundMode` | `0x34470` | 175 | UnwindData |  |
| 6 | `UbpmReleaseJobBackgroundMode` | `0x34530` | 157 | UnwindData |  |
| 11 | `UbpmTriggerConsumerControlNotifications` | `0x345E0` | 190 | UnwindData |  |
| 14 | `UbpmTriggerConsumerSetDisabledForUser` | `0x346B0` | 183 | UnwindData |  |
