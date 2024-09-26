import bentoml
from bentoml.adapters import JsonInput
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact
from sinara.bentoservice.binary_artifact import BinaryFileArtifact
import catboost

@bentoml.env(infer_pip_packages=True)
@bentoml.artifacts([
    SklearnModelArtifact('model'),
    BinaryFileArtifact('some_model_binary_artifact')
])

class TestService(bentoml.BentoService):
    """
    TestService is designed for...
    """

    @bentoml.api(input=DataframeInput(), batch=True)
    def predict(self, df):
        return self.artifacts.model.predict(df)