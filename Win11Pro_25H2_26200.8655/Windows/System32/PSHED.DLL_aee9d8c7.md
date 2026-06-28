# Binary Specification: PSHED.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\PSHED.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aee9d8c7c9041eac3f6208a84e10a04eca0aa735b4a1a1f24d252c088cb1a720`
* **Total Exported Functions:** 35

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `PshedArePluginsPresent` | `0x1150` | 13 | UnwindData |  |
| 4 | `PshedAttemptErrorRecovery` | `0x1170` | 189 | UnwindData |  |
| 5 | `PshedBugCheckSystem` | `0x1240` | 22 | UnwindData |  |
| 6 | `PshedClearErrorRecord` | `0x1260` | 187 | UnwindData |  |
| 7 | `PshedDisableErrorSource` | `0x1330` | 191 | UnwindData |  |
| 10 | `PshedEnableErrorSource` | `0x1400` | 168 | UnwindData |  |
| 11 | `PshedFinalizeErrorRecord` | `0x14B0` | 169 | UnwindData |  |
| 14 | `PshedGetBootErrorPacket` | `0x1560` | 290 | UnwindData |  |
| 15 | `PshedGetErrorSourceInfo` | `0x1690` | 188 | UnwindData |  |
| 17 | `PshedGetInjectionCapabilities` | `0x1760` | 276 | UnwindData |  |
| 23 | `PshedInjectError` | `0x1880` | 354 | UnwindData |  |
| 24 | `PshedIsSystemWheaEnabled` | `0x19F0` | 8 | UnwindData |  |
| 25 | `PshedMarkHiberPhase` | `0x1A00` | 99 | UnwindData |  |
| 26 | `PshedReadErrorRecord` | `0x1A70` | 197 | UnwindData |  |
| 28 | `PshedRetrieveErrorInfo` | `0x1B40` | 242 | UnwindData |  |
| 29 | `PshedSetErrorSourceInfo` | `0x1C40` | 188 | UnwindData |  |
| 32 | `PshedTranslateDimmAddress` | `0x1D10` | 172 | UnwindData |  |
| 33 | `PshedTranslatePhysicalAddress` | `0x1DD0` | 173 | UnwindData |  |
| 35 | `PshedWriteErrorRecord` | `0x1E90` | 349 | UnwindData |  |
| 8 | `PshedDoPfa` | `0x2BA0` | 58 | UnwindData |  |
| 16 | `PshedGetHalEnlightenments` | `0x2BE0` | 13 | UnwindData |  |
| 19 | `PshedInitAvailable` | `0x2C00` | 13 | UnwindData |  |
| 20 | `PshedInitGlobal` | `0x2C20` | 41 | UnwindData |  |
| 21 | `PshedInitProc` | `0x2C50` | 41 | UnwindData |  |
| 30 | `PshedSetHalEnlightenments` | `0x2C80` | 13 | UnwindData |  |
| 31 | `PshedSynchronizeExecution` | `0x2CA0` | 4 | UnwindData |  |
| 1 | `PshedAddToDefectList` | `0xD010` | 205 | UnwindData |  |
| 13 | `PshedGetAllErrorSources` | `0xD0F0` | 310 | UnwindData |  |
| 18 | `PshedGetMemoryDetails` | `0xD230` | 120 | UnwindData |  |
| 2 | `PshedAllocateMemory` | `0xD610` | 35 | UnwindData |  |
| 9 | `PshedDoPluginCtl` | `0xD640` | 196 | UnwindData |  |
| 12 | `PshedFreeMemory` | `0xD710` | 27 | UnwindData |  |
| 27 | `PshedRegisterPlugin` | `0xD740` | 1,514 | UnwindData |  |
| 34 | `PshedUnregisterPlugin` | `0xDD30` | 275 | UnwindData |  |
| 22 | `PshedInitialize` | `0x104F0` | 586 | UnwindData |  |
