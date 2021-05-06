from abc import ABC, abstractmethod

class Backend(ABC):

    @abstractmethod
    def add_middleware_handler(self, handler):
        pass

    @abstractmethod
    def add_message_handler(self, handler):
        pass

    @abstractmethod
    def add_edited_message_handler(self, handler):
        pass

    @abstractmethod
    def add_chanel_post_handler(self, handler):
        pass

    @abstractmethod
    def add_edited_chanel_post_handler(self, handler):
        pass
    
    @abstractmethod
    def add_inline_handler(self,handler):
        pass
    
    @abstractmethod
    def add_chosen_inline_handler(self, handler):
        pass

    @abstractmethod
    def add_callback_query_handler(self, handler):
        pass

    @abstractmethod
    def add_shipping_query_handler(self, handler):
        pass
    
    @abstractmethod
    def add_pre_checkout_query_handler(self, handler):
        pass

    @abstractmethod
    def add_poll_handler(self, handler):
        pass

    @abstractmethod
    def add_poll_answer_handler(self, handler):
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        pass







