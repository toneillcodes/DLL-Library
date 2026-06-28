# Binary Specification: TextInputMethodFormatter.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\TextInputMethodFormatter.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7c51c40bade488fd0dad804b36bfe474f6c87b9d5b459feb09ca1b9183456691`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `??0TextInputMethodFormatter@@QEAA@XZ` | `0x4430` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??1TextInputMethodFormatter@@QEAA@XZ` | `0x48D0` | 669 | UnwindData |  |
| 8 | `?GetIsHost@TextInputMethodFormatter@@UEAA_NXZ` | `0x5B00` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?GetTVIImpl@TextInputMethodFormatter@@UEAAJPEAPEAUITextVirtualizationInternal@@@Z` | `0x6470` | 12,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?SetCIVMTarget@TextInputMethodFormatter@@UEAAJPEAUIRemoteCoreInputViewManager@@@Z` | `0x6470` | 12,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?SetTISTarget@TextInputMethodFormatter@@UEAAJPEAUIRemoteTextInputServer@@@Z` | `0x6470` | 12,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0TextInputMethodFormatter@@QEAA@PEAUITextVirtualizationKeyRoutingServerCallback@@@Z` | `0x93F0` | 5,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?ContinueDeserialize@TextInputMethodFormatter@@QEAAJGAEAV?$vector@DV?$allocator@D@std@@@std@@@Z` | `0xA880` | 72 | UnwindData |  |
| 5 | `?DataReceived@TextInputMethodFormatter@@UEAAJIAEAV?$vector@DV?$allocator@D@std@@@std@@@Z` | `0xA960` | 489 | UnwindData |  |
| 6 | `?GetCIVMSender@TextInputMethodFormatter@@UEAAJPEAPEAUIRemoteCoreInputViewManager@@@Z` | `0xB920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?GetCIVSender@TextInputMethodFormatter@@UEAAJPEAPEAUIRemoteCoreInputView@@@Z` | `0xB940` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?GetVirtTIS@TextInputMethodFormatter@@QEAAJPEAPEAUIRemoteTextInputServer@@@Z` | `0xB940` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?GetPduIdHelper@TextInputMethodFormatter@@QEAAJPEAPEAX@Z` | `0xBD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?GetRemoteImeOpsQueue@TextInputMethodFormatter@@UEAAJPEAPEAUIRemoteImeOperationsQueue@@@Z` | `0xBD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?GetTICImpl@TextInputMethodFormatter@@UEAAJPEAPEAUIRemoteTextInputClient@@@Z` | `0xBDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?GetTISImpl@TextInputMethodFormatter@@UEAAJPEAPEAUIRemoteTextInputServer@@@Z` | `0xBDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?GetTVKRImpl@TextInputMethodFormatter@@UEAAJPEAPEAUITextVirtualizationKeyRouting@@@Z` | `0xBDE0` | 357 | UnwindData |  |
| 16 | `?Initialize@TextInputMethodFormatter@@QEAAJPEAUIMessagePort@@PEAUIMessageSession@@W4VirtualizationEnvironment@@PEAUIVirtualizedTextDataSender@@U_GUID@@@Z` | `0xC0B0` | 669 | UnwindData |  |
| 17 | `?Initialize@TextInputMethodFormatter@@UEAAJPEAUIMessagePort@@PEAUIMessageSession@@@Z` | `0xC360` | 51 | UnwindData |  |
| 18 | `?PeekPayloadPdu@TextInputMethodFormatter@@QEAAJAEAV?$vector@DV?$allocator@D@std@@@std@@PEAUKeyEventPayloadInfo@@@Z` | `0xCEF0` | 215 | UnwindData |  |
| 19 | `?ProcessQueue@TextInputMethodFormatter@@QEAAJXZ` | `0xD070` | 386 | UnwindData |  |
| 21 | `?SetCIVTarget@TextInputMethodFormatter@@UEAAJPEAUIRemoteCoreInputView@@PEAVVirtCoreInputViewForwarder@@@Z` | `0xF6C0` | 186 | UnwindData |  |
| 22 | `?SetRemoteImeOpsQueue@TextInputMethodFormatter@@UEAAJPEAUIRemoteImeOperationsQueue@@@Z` | `0xF7B0` | 70 | UnwindData |  |
| 23 | `?SetTICTarget@TextInputMethodFormatter@@UEAAJPEAUIRemoteTextInputClient@@PEAVVirtTextInputClient@@@Z` | `0xF830` | 219 | UnwindData |  |
| 24 | `?SetTIHTarget@TextInputMethodFormatter@@UEAAJPEAVVirtTextInputHost@@@Z` | `0xF920` | 518 | UnwindData |  |
| 26 | `?SetTVKRTarget@TextInputMethodFormatter@@UEAAJPEAUITextVirtualizationKeyRouting@@@Z` | `0xFB30` | 396 | UnwindData |  |
| 27 | `?TryConnect@TextInputMethodFormatter@@QEAAJXZ` | `0x10300` | 152 | UnwindData |  |
| 28 | `?Uninitialize@TextInputMethodFormatter@@UEAAJ_N@Z` | `0x103F0` | 228 | UnwindData |  |
| 29 | `DllCanUnloadNow` | `0x10FF0` | 97 | UnwindData |  |
| 30 | `DllGetActivationFactory` | `0x11060` | 466 | UnwindData |  |
| 31 | `DllGetClassObject` | `0x11240` | 288 | UnwindData |  |
