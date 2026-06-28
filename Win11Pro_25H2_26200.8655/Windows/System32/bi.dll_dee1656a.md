# Binary Specification: bi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\bi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dee1656addd79759e036908c24bfeb063caaa857a0ba1239fca353179792b616`
* **Total Exported Functions:** 35

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BiActivateDeferredWorkItem` | `0x1910` | 140 | UnwindData |  |
| 2 | `BiActivateInBackground` | `0x19B0` | 113 | UnwindData |  |
| 3 | `BiActivateInBackgroundEx` | `0x1A30` | 604 | UnwindData |  |
| 4 | `BiActivateWorkItem` | `0x1CA0` | 142 | UnwindData |  |
| 5 | `BiAssociateActivationProxy` | `0x1D40` | 288 | UnwindData |  |
| 6 | `BiAssociateApplicationExtensionClass` | `0x1E70` | 312 | UnwindData |  |
| 7 | `BiCancelWorkItem` | `0x1FB0` | 147 | UnwindData |  |
| 8 | `BiCancelWorkItemEx` | `0x2050` | 157 | UnwindData |  |
| 9 | `BiCreateEvent` | `0x2100` | 330 | UnwindData |  |
| 10 | `BiCreateEventForPackageName` | `0x2250` | 319 | UnwindData |  |
| 11 | `BiDeleteEvent` | `0x23A0` | 142 | UnwindData |  |
| 12 | `BiDisassociateWorkItem` | `0x2440` | 158 | UnwindData |  |
| 13 | `BiDiscardPendingActivations` | `0x24F0` | 142 | UnwindData |  |
| 14 | `BiEnumerateBrokeredEvents` | `0x2590` | 178 | UnwindData |  |
| 15 | `BiEnumerateUserContexts` | `0x2650` | 159 | UnwindData |  |
| 16 | `BiEnumerateUserSessions` | `0x2700` | 159 | UnwindData |  |
| 17 | `BiEnumerateWorkItemsForPackageName` | `0x27B0` | 250 | UnwindData |  |
| 18 | `BiEnumerateWorkItemsForPackageNameEx` | `0x28B0` | 259 | UnwindData |  |
| 19 | `BiFreeMemory` | `0x29C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `BiPackageChangeState` | `0x29F0` | 230 | UnwindData |  |
| 21 | `BiQueryBrokeredEvent` | `0x2AE0` | 178 | UnwindData |  |
| 22 | `BiQuerySystemStateBroadcastChannels` | `0x2BA0` | 142 | UnwindData |  |
| 23 | `BiQueryUserContext` | `0x2C40` | 178 | UnwindData |  |
| 24 | `BiQueryUserSession` | `0x2D00` | 157 | UnwindData |  |
| 25 | `BiQueryWorkItem` | `0x2DB0` | 183 | UnwindData |  |
| 26 | `BiQueryWorkItemEx` | `0x2E70` | 196 | UnwindData |  |
| 27 | `BiQueryWorkItemStatusStateName` | `0x2F40` | 159 | UnwindData |  |
| 29 | `BiSignalEventEx` | `0x2FF0` | 223 | UnwindData |  |
| 30 | `BiSignalMultipleEvents` | `0x30E0` | 223 | UnwindData |  |
| 31 | `BiSignalTriggerEvent` | `0x31D0` | 29 | UnwindData |  |
| 32 | `BiSignalTriggerEventEx` | `0x3200` | 223 | UnwindData |  |
| 33 | `BiUpdateEventFlags` | `0x32F0` | 175 | UnwindData |  |
| 34 | `BiUpdateEventInformation` | `0x33B0` | 177 | UnwindData |  |
| 35 | `BiUpdateEventParameters` | `0x3470` | 159 | UnwindData |  |
| 28 | `BiSignalEvent` | `0x3520` | 29 | UnwindData |  |
