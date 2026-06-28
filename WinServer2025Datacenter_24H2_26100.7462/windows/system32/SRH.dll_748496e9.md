# Binary Specification: SRH.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SRH.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `748496e967725aa1c9e12e216512a4df96c010c3c6ca6ce87756cd18a3fb08f8`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 28 | `StartIgnoringLeaks` | `0x3F520` | 12,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `StopIgnoringLeaks` | `0x3F520` | 12,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x426D0` | 82 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x42730` | 45 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x42770` | 151 | UnwindData |  |
| 5 | `DllMain` | `0x42810` | 245 | UnwindData |  |
| 1 | `CreateAndEnqueueNarratorCommandEvent` | `0x45890` | 364 | UnwindData |  |
| 6 | `ExecuteNarratorFind` | `0x45A10` | 196 | UnwindData |  |
| 7 | `GetInputLearningHelper` | `0x45AE0` | 47 | UnwindData |  |
| 8 | `HandleNarratorUIAction` | `0x45B20` | 38 | UnwindData |  |
| 9 | `IgnoreLeaksInCurrentlyTrackedMemory` | `0x45B50` | 18 | UnwindData |  |
| 10 | `Initialize` | `0x45B70` | 110 | UnwindData |  |
| 11 | `IsIgnoringLeaks` | `0x45BF0` | 21 | UnwindData |  |
| 12 | `PostTestCheckForLeaks` | `0x45C10` | 18 | UnwindData |  |
| 13 | `QueryLanguageModel` | `0x45C30` | 195 | UnwindData |  |
| 14 | `RunNarrator` | `0x45D00` | 312 | UnwindData |  |
| 15 | `SaveConfiguration` | `0x45E40` | 122 | UnwindData |  |
| 16 | `SetBrailleBlinkingCursor` | `0x45EC0` | 120 | UnwindData |  |
| 17 | `SetBrailleCursorRepresentation` | `0x45F40` | 118 | UnwindData |  |
| 18 | `SetBrailleDeviceChangeFromReg` | `0x45FC0` | 71 | UnwindData |  |
| 19 | `SetBrailleIsEnabledFromReg` | `0x46010` | 250 | UnwindData |  |
| 20 | `SetBrailleTablesFromReg` | `0x46110` | 87 | UnwindData |  |
| 21 | `SetDictationRunning` | `0x46170` | 98 | UnwindData |  |
| 22 | `SetFastKeyEntryEnabled` | `0x461E0` | 101 | UnwindData |  |
| 23 | `SetFollowInsertion` | `0x46250` | 101 | UnwindData |  |
| 24 | `SetReadHints` | `0x462C0` | 101 | UnwindData |  |
| 25 | `SetScriptingEnabledFromReg` | `0x46330` | 244 | UnwindData |  |
| 26 | `SetVoicePropertiesFromReg` | `0x46430` | 91 | UnwindData |  |
| 27 | `SpeakConfiguration` | `0x464A0` | 235 | UnwindData |  |
| 30 | `UpdateErrorLoggingCallback` | `0x46890` | 18 | UnwindData |  |
| 31 | `UpdateNarratorSettingsFromReg` | `0x468B0` | 391 | UnwindData |  |
