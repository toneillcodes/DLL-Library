# Binary Specification: JpMapControl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\JpMapControl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `20bff8c80b4aff036789c0e88daac6b4515eb8b2fe9a652aa1bfe82c820ef647`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3E80` | 32 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x3EB0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3EF0` | 65 | UnwindData |  |
| 4 | `JpIs3DSupported` | `0x28D60` | 173 | UnwindData |  |
| 5 | `JpIsUnifiedMapsStack` | `0x28E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `JpMapControl_Create` | `0x28E30` | 210 | UnwindData |  |
| 9 | `JpMapModel3DFrom3MFStreamOperation_Create` | `0x28F10` | 246 | UnwindData |  |
| 12 | `JpOverviewMapControl_Create` | `0x29010` | 194 | UnwindData |  |
| 13 | `JpRestrictedApiAccessCheck` | `0x290E0` | 62 | UnwindData |  |
| 14 | `JpStreetsideExperience_Create` | `0x29130` | 213 | UnwindData |  |
| 15 | `JpStreetsidePanoramaOperation_Create` | `0x29210` | 258 | UnwindData |  |
| 6 | `JpMapControlSettings_Create` | `0x29A10` | 164 | UnwindData |  |
| 16 | `MapSettings_GetMosBingMapsKey` | `0x29AC0` | 230 | UnwindData |  |
| 17 | `MapSettings_ResetMosKeys` | `0x29BB0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `JpMapFactory_Create` | `0x29FF0` | 171 | UnwindData |  |
| 10 | `JpMapOverlayModel_Create` | `0x2D680` | 192 | UnwindData |  |
| 11 | `JpMapStyleSheetFactory_Create` | `0x2DD30` | 174 | UnwindData |  |
