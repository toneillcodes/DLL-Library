# Binary Specification: FaceProcessor.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\helloface.inf_amd64_5a5e79362aedc5e6\FaceProcessor.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e25a3ffe4c12992e2f1b535f790d36bb0542a89753c519b4b9f68e0b853dbe7e`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CreateFacePreprocessorOutput` | `0x52770` | 1,255 | UnwindData |  |
| 1 | `CreateColorFaceProcessor` | `0x74AA0` | 1,488 | UnwindData |  |
| 3 | `FileInputManager_InitializeRuntime` | `0x75B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FileInputManager_ReadSourceColorFrameData` | `0x75B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FileInputManager_ReadSourceDeviceMetadata` | `0x75B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FileInputManager_ReadSourceInfraredFrameData` | `0x75B90` | 29 | UnwindData |  |
| 7 | `FileInputManager_Reset` | `0x75BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `FileInputManager_SendColorFrameData` | `0x75BD0` | 46 | UnwindData |  |
| 9 | `FileInputManager_SendInfraredFrameData` | `0x75C10` | 65 | UnwindData |  |
