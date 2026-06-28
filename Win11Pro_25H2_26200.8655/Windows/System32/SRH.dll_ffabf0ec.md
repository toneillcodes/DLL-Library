# Binary Specification: SRH.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SRH.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ffabf0eccaf2de96dfe6669d4018903152787462d275c3137983e778a79fc051`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 31 | `StartIgnoringLeaks` | `0x443B0` | 13,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `StopIgnoringLeaks` | `0x443B0` | 13,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllCanUnloadNow` | `0x47A20` | 82 | UnwindData |  |
| 4 | `DllGetActivationFactory` | `0x47A80` | 45 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x47AC0` | 151 | UnwindData |  |
| 6 | `DllMain` | `0x47B60` | 261 | UnwindData |  |
| 1 | `CleanupLanguageModel` | `0x530E0` | 17 | UnwindData |  |
| 2 | `CreateAndEnqueueNarratorCommandEvent` | `0x53100` | 364 | UnwindData |  |
| 7 | `ExecuteNarratorFind` | `0x53280` | 196 | UnwindData |  |
| 8 | `GetInputLearningHelper` | `0x53350` | 47 | UnwindData |  |
| 9 | `HandleNarratorUIAction` | `0x53390` | 38 | UnwindData |  |
| 10 | `IgnoreLeaksInCurrentlyTrackedMemory` | `0x533C0` | 18 | UnwindData |  |
| 11 | `Initialize` | `0x533E0` | 110 | UnwindData |  |
| 12 | `IsIgnoringLeaks` | `0x53460` | 21 | UnwindData |  |
| 13 | `PostTestCheckForLeaks` | `0x53480` | 18 | UnwindData |  |
| 14 | `QueryLanguageModel` | `0x534A0` | 533 | UnwindData |  |
| 15 | `ResetConfiguration` | `0x536C0` | 123 | UnwindData |  |
| 16 | `RetryModelDownload` | `0x53750` | 65 | UnwindData |  |
| 17 | `RunNarrator` | `0x537A0` | 717 | UnwindData |  |
| 18 | `SaveConfiguration` | `0x53A80` | 387 | UnwindData |  |
| 19 | `SetBrailleBlinkingCursor` | `0x53C10` | 120 | UnwindData |  |
| 20 | `SetBrailleCursorRepresentation` | `0x53C90` | 118 | UnwindData |  |
| 21 | `SetBrailleDeviceChangeFromReg` | `0x53D10` | 71 | UnwindData |  |
| 22 | `SetBrailleIsEnabledFromReg` | `0x53D60` | 250 | UnwindData |  |
| 23 | `SetBrailleTablesFromReg` | `0x53E60` | 87 | UnwindData |  |
| 24 | `SetDictationRunning` | `0x53EC0` | 98 | UnwindData |  |
| 25 | `SetFastKeyEntryEnabled` | `0x53F30` | 101 | UnwindData |  |
| 26 | `SetFollowInsertion` | `0x53FA0` | 101 | UnwindData |  |
| 27 | `SetNarratorLaunchStartTime` | `0x54010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `SetReadHints` | `0x54020` | 101 | UnwindData |  |
| 29 | `SetScriptingEnabledFromReg` | `0x54090` | 446 | UnwindData |  |
| 30 | `SetVoicePropertiesFromReg` | `0x54260` | 91 | UnwindData |  |
| 33 | `UpdateErrorLoggingCallback` | `0x545C0` | 18 | UnwindData |  |
| 34 | `UpdateNarratorSettingsFromReg` | `0x545E0` | 391 | UnwindData |  |
